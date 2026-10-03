"""
Banking Application
--------------------
A command-line bank built with Python OOP.

Concepts demonstrated:
  - Classes & objects (Transaction, Account, Bank, BankApp)
  - Encapsulation (balance only changes through credit/debit methods)
  - Custom exceptions (BankError and friends)
  - Password hashing with a salt (passwords are never stored in plain text)
  - File persistence with JSON (data survives restarts)
  - Input validation, loops, functions, string formatting, datetime

Features:
  Create account | Login | Deposit | Withdraw | Transfer | Balance
  Transaction history (with filters) | Account statement
  Change password | Reset password (security question)
  Profile management | Airtime purchase | Close account
  Daily withdrawal limit | Account lockout after failed logins
"""

import hashlib
import hmac
import json
import os
import random
import re
import secrets
from datetime import datetime

# ----------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------
DATA_FILE = "bank_data.json"
CURRENCY = "₦"
MIN_AMOUNT = 1
DAILY_WITHDRAWAL_LIMIT = 500_000
MAX_LOGIN_ATTEMPTS = 3
MIN_PASSWORD_LENGTH = 8
ACCOUNT_TYPES = {"1": "Savings", "2": "Current"}
SECURITY_QUESTIONS = [
    "What is your mother's maiden name?",
    "What was the name of your first school?",
    "What is the name of your childhood best friend?",
    "In what town were you born?",
]


# ----------------------------------------------------------------------------
# Custom exceptions
# ----------------------------------------------------------------------------
class BankError(Exception):
    """Base class for all expected banking errors."""


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class WithdrawalLimitError(BankError):
    pass


# ----------------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------------
def money(amount):
    """Format a number as money, e.g. ₦1,250.50"""
    return f"{CURRENCY}{amount:,.2f}"


def hash_secret(secret, salt=None):
    """Hash a password / security answer with a random salt (PBKDF2)."""
    salt = salt or secrets.token_hex(8)
    digest = hashlib.pbkdf2_hmac("sha256", secret.encode(), salt.encode(), 100_000).hex()
    return f"{salt}${digest}"


def verify_secret(secret, stored):
    """Check a plain-text secret against its stored salted hash."""
    salt, _ = stored.split("$")
    return hmac.compare_digest(hash_secret(secret, salt), stored)


def valid_email(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


def valid_phone(phone):
    return re.fullmatch(r"\d{10,14}", phone) is not None


def password_problem(password):
    """Return a message describing what's wrong with the password, or None."""
    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Password must be at least {MIN_PASSWORD_LENGTH} characters."
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        return "Password must contain both letters and numbers."
    return None


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------------------------
# Transaction
# ----------------------------------------------------------------------------
class Transaction:
    def __init__(self, kind, amount, balance_after, description,
                 reference=None, timestamp=None):
        self.kind = kind                      # Deposit, Withdrawal, Transfer In, ...
        self.amount = amount
        self.balance_after = balance_after
        self.description = description
        self.reference = reference or secrets.token_hex(5).upper()
        self.timestamp = timestamp or now()

    @property
    def is_credit(self):
        return self.kind in ("Deposit", "Transfer In")

    def to_dict(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        sign = "+" if self.is_credit else "-"
        return (f"{self.timestamp} | {self.reference:<10} | {self.kind:<12} | "
                f"{sign}{money(self.amount):>14} | Bal: {money(self.balance_after):>14} | "
                f"{self.description}")


# ----------------------------------------------------------------------------
# Account
# ----------------------------------------------------------------------------
class Account:
    def __init__(self, fullname, email, phone, password_hash, account_number,
                 account_type, security_question, security_answer_hash,
                 balance=0.0, transactions=None, failed_attempts=0,
                 locked=False, created_at=None):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.password_hash = password_hash
        self.account_number = account_number
        self.account_type = account_type
        self.security_question = security_question
        self.security_answer_hash = security_answer_hash
        self._balance = balance                       # "private": use the methods
        self.transactions = transactions or []
        self.failed_attempts = failed_attempts
        self.locked = locked
        self.created_at = created_at or now()

    # ----- balance (read-only from outside) -----
    @property
    def balance(self):
        return self._balance

    # ----- security -----
    def check_password(self, password):
        return verify_secret(password, self.password_hash)

    def set_password(self, new_password):
        self.password_hash = hash_secret(new_password)
        self.failed_attempts = 0
        self.locked = False

    def check_security_answer(self, answer):
        return verify_secret(answer.strip().lower(), self.security_answer_hash)

    # ----- money movement -----
    @staticmethod
    def _validate_amount(amount):
        if amount < MIN_AMOUNT:
            raise InvalidAmountError(f"Amount can't be less than {money(MIN_AMOUNT)}.")

    def credit(self, amount, kind="Deposit", description="Cash deposit", reference=None):
        self._validate_amount(amount)
        self._balance += amount
        txn = Transaction(kind, amount, self._balance, description, reference)
        self.transactions.append(txn)
        return txn

    def debit(self, amount, kind="Withdrawal", description="Cash withdrawal", reference=None):
        self._validate_amount(amount)
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        if kind == "Withdrawal":
            remaining = DAILY_WITHDRAWAL_LIMIT - self.withdrawn_today()
            if amount > remaining:
                raise WithdrawalLimitError(
                    f"Daily withdrawal limit exceeded. You can still withdraw {money(max(remaining, 0))} today."
                )
        self._balance -= amount
        txn = Transaction(kind, amount, self._balance, description, reference)
        self.transactions.append(txn)
        return txn

    def withdrawn_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(t.amount for t in self.transactions
                   if t.kind == "Withdrawal" and t.timestamp.startswith(today))

    # ----- (de)serialisation -----
    def to_dict(self):
        data = self.__dict__.copy()
        data["balance"] = data.pop("_balance")
        data["transactions"] = [t.to_dict() for t in self.transactions]
        return data

    @classmethod
    def from_dict(cls, data):
        data = data.copy()
        data["transactions"] = [Transaction.from_dict(t) for t in data["transactions"]]
        return cls(**data)


# ----------------------------------------------------------------------------
# Bank (business logic + storage)
# ----------------------------------------------------------------------------
class Bank:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.accounts = []
        self.load()

    # ----- storage -----
    def load(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.accounts = [Account.from_dict(a) for a in json.load(f)]
        except (json.JSONDecodeError, TypeError, KeyError):
            print("⚠️  Could not read saved data. Starting with an empty database.")
            self.accounts = []

    def save(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([a.to_dict() for a in self.accounts], f, indent=2)

    # ----- lookups -----
    def find_by_email(self, email):
        return next((a for a in self.accounts if a.email == email), None)

    def find_by_account_number(self, number):
        return next((a for a in self.accounts if a.account_number == number), None)

    def _new_account_number(self):
        while True:
            number = "".join(random.choices("0123456789", k=10))
            if not self.find_by_account_number(number):
                return number

    # ----- operations -----
    def register(self, fullname, email, phone, password, account_type,
                 question, answer):
        account = Account(
            fullname=fullname,
            email=email,
            phone=phone,
            password_hash=hash_secret(password),
            account_number=self._new_account_number(),
            account_type=account_type,
            security_question=question,
            security_answer_hash=hash_secret(answer.strip().lower()),
        )
        self.accounts.append(account)
        self.save()
        return account

    def authenticate(self, email, password):
        """Return the account if credentials are right. Locks after too many failures."""
        account = self.find_by_email(email)
        if not account:
            raise BankError("Invalid email or password.")
        if account.locked:
            raise BankError("This account is locked. Use 'Reset password' to unlock it.")
        if not account.check_password(password):
            account.failed_attempts += 1
            if account.failed_attempts >= MAX_LOGIN_ATTEMPTS:
                account.locked = True
                self.save()
                raise BankError("Too many failed attempts. Account locked. Reset your password to unlock it.")
            self.save()
            left = MAX_LOGIN_ATTEMPTS - account.failed_attempts
            raise BankError(f"Invalid email or password. {left} attempt(s) left.")
        account.failed_attempts = 0
        self.save()
        return account

    def transfer(self, sender, account_number, amount):
        receiver = self.find_by_account_number(account_number)
        if not receiver:
            raise BankError("Recipient account not found.")
        if receiver is sender:
            raise BankError("You can't transfer to your own account.")
        reference = secrets.token_hex(5).upper()   # same reference on both sides
        sender.debit(amount, "Transfer Out",
                     f"To {receiver.fullname} ({receiver.account_number})", reference)
        receiver.credit(amount, "Transfer In",
                        f"From {sender.fullname} ({sender.account_number})", reference)
        self.save()
        return receiver, reference

    def delete_account(self, account):
        self.accounts.remove(account)
        self.save()


# ----------------------------------------------------------------------------
# Command-line interface
# ----------------------------------------------------------------------------
class BankApp:
    def __init__(self):
        self.bank = Bank()

    # ----- input helpers -----
    @staticmethod
    def ask_amount(prompt="Amount: "):
        while True:
            raw = input(prompt).strip().replace(",", "")
            if raw.lower() in ("c", "cancel"):
                return None
            try:
                return float(raw)
            except ValueError:
                print("❌ Enter a valid number (or 'c' to cancel).")

    @staticmethod
    def ask_new_password():
        while True:
            password = input("New password: ").strip()
            problem = password_problem(password)
            if problem:
                print(f"❌ {problem}")
                continue
            if input("Confirm password: ").strip() != password:
                print("❌ Passwords don't match.")
                continue
            return password

    @staticmethod
    def confirm_password(account, message="Enter your password to confirm: "):
        if account.check_password(input(message).strip()):
            return True
        print("❌ Incorrect password.")
        return False

    # ----- registration -----
    def create_account(self):
        print("\n--- Create Account ---")
        fullname = input("Full name: ").strip().title()
        email = input("Email: ").strip().lower()
        phone = input("Phone number (digits only): ").strip()

        if not fullname or not email or not phone:
            print("❌ All fields are required.")
            return
        if not valid_email(email):
            print("❌ Invalid email address.")
            return
        if not valid_phone(phone):
            print("❌ Phone number must be 10 to 14 digits.")
            return
        if self.bank.find_by_email(email):
            print("❌ An account with this email already exists.")
            return

        print("\nAccount type:  1. Savings   2. Current")
        account_type = ACCOUNT_TYPES.get(input("Choice: ").strip())
        if not account_type:
            print("❌ Invalid account type.")
            return

        password = input("Password: ").strip()
        confirm = input("Confirm password: ").strip()
        problem = password_problem(password)
        if problem:
            print(f"❌ {problem}")
            return
        if password != confirm:
            print("❌ Passwords don't match.")
            return

        print("\nChoose a security question (used to reset your password):")
        for i, q in enumerate(SECURITY_QUESTIONS, 1):
            print(f"  {i}. {q}")
        pick = input("Choice: ").strip()
        if not pick.isdigit() or not 1 <= int(pick) <= len(SECURITY_QUESTIONS):
            print("❌ Invalid choice.")
            return
        question = SECURITY_QUESTIONS[int(pick) - 1]
        answer = input("Answer: ").strip()
        if not answer:
            print("❌ Answer is required.")
            return

        account = self.bank.register(fullname, email, phone, password,
                                     account_type, question, answer)
        print("\n✅ Registration successful!")
        print(f"   Your {account.account_type} account number is: {account.account_number}")

    # ----- login / reset -----
    def login(self):
        print("\n--- Login ---")
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        try:
            account = self.bank.authenticate(email, password)
        except BankError as e:
            print(f"❌ {e}")
            return
        print(f"\n✅ Login successful. Welcome, {account.fullname}!")
        self.account_menu(account)

    def reset_password(self):
        print("\n--- Reset Password ---")
        email = input("Email: ").strip().lower()
        account = self.bank.find_by_email(email)
        if not account:
            print("❌ No account found with that email.")
            return
        print(f"Security question: {account.security_question}")
        if not account.check_security_answer(input("Answer: ")):
            print("❌ Incorrect answer.")
            return
        account.set_password(self.ask_new_password())   # also unlocks the account
        self.bank.save()
        print("✅ Password reset successful. You can now log in.")

    # ----- account actions -----
    def deposit(self, account):
        amount = self.ask_amount("Deposit amount (c to cancel): ")
        if amount is None:
            return
        try:
            txn = account.credit(amount)
        except BankError as e:
            print(f"❌ {e}")
            return
        self.bank.save()
        print(f"✅ You've deposited {money(amount)}. Ref: {txn.reference}")
        print(f"   Account balance: {money(account.balance)}")

    def withdraw(self, account):
        amount = self.ask_amount("Withdrawal amount (c to cancel): ")
        if amount is None:
            return
        try:
            txn = account.debit(amount)
        except BankError as e:
            print(f"❌ {e}")
            return
        self.bank.save()
        print(f"✅ You've withdrawn {money(amount)}. Ref: {txn.reference}")
        print(f"   Account balance: {money(account.balance)}")

    def transfer(self, account):
        number = input("Recipient account number: ").strip()
        receiver = self.bank.find_by_account_number(number)
        if not receiver:
            print("❌ Recipient account not found.")
            return
        if receiver is account:
            print("❌ You can't transfer to your own account.")
            return
        print(f"Recipient: {receiver.fullname}")
        amount = self.ask_amount("Transfer amount (c to cancel): ")
        if amount is None:
            return
        if amount > account.balance:
            print("❌ Insufficient funds.")
            return
        if amount < MIN_AMOUNT:
            print(f"❌ Amount can't be less than {money(MIN_AMOUNT)}.")
            return
        if input(f"Send {money(amount)} to {receiver.fullname}? (y/n): ").strip().lower() != "y":
            print("Transfer cancelled.")
            return
        if not self.confirm_password(account):
            return
        try:
            _, ref = self.bank.transfer(account, number, amount)
        except BankError as e:
            print(f"❌ {e}")
            return
        print(f"✅ Transfer successful! Ref: {ref}")
        print(f"   Account balance: {money(account.balance)}")

    def check_balance(self, account):
        print(f"\nAccount: {account.account_number} ({account.account_type})")
        print(f"Balance: {money(account.balance)}")
        left = DAILY_WITHDRAWAL_LIMIT - account.withdrawn_today()
        print(f"Withdrawal allowance left today: {money(max(left, 0))}")

    def buy_airtime(self, account):
        phone = input("Phone number: ").strip()
        if not valid_phone(phone):
            print("❌ Invalid phone number.")
            return
        amount = self.ask_amount("Airtime amount (c to cancel): ")
        if amount is None:
            return
        try:
            txn = account.debit(amount, "Airtime", f"Airtime for {phone}")
        except BankError as e:
            print(f"❌ {e}")
            return
        self.bank.save()
        print(f"✅ {money(amount)} airtime sent to {phone}. Ref: {txn.reference}")
        print(f"   Account balance: {money(account.balance)}")

    # ----- history / statement -----
    @staticmethod
    def print_transactions(transactions):
        if not transactions:
            print("No transactions found.")
            return
        print("-" * 118)
        for t in transactions:
            print(t)
        print("-" * 118)

    def transaction_history(self, account):
        print("""
        1. Last 5 transactions
        2. All transactions
        3. Filter by type
        4. Filter by date (YYYY-MM-DD)
        """)
        choice = input("Choice: ").strip()
        history = list(reversed(account.transactions))       # newest first
        if choice == "1":
            self.print_transactions(history[:5])
        elif choice == "2":
            self.print_transactions(history)
        elif choice == "3":
            kinds = sorted({t.kind for t in account.transactions})
            if not kinds:
                print("No transactions yet.")
                return
            print("Types:", ", ".join(kinds))
            kind = input("Type: ").strip().lower()
            self.print_transactions([t for t in history if t.kind.lower() == kind])
        elif choice == "4":
            day = input("Date: ").strip()
            self.print_transactions([t for t in history if t.timestamp.startswith(day)])
        else:
            print("Invalid choice.")

    def statement(self, account):
        credits = sum(t.amount for t in account.transactions if t.is_credit)
        debits = sum(t.amount for t in account.transactions if not t.is_credit)
        print("\n" + "=" * 50)
        print("ACCOUNT STATEMENT".center(50))
        print("=" * 50)
        print(f"Name           : {account.fullname}")
        print(f"Account number : {account.account_number} ({account.account_type})")
        print(f"Generated on   : {now()}")
        print(f"Total credits  : {money(credits)}")
        print(f"Total debits   : {money(debits)}")
        print(f"Closing balance: {money(account.balance)}")
        print("=" * 50)
        self.print_transactions(account.transactions)

    # ----- security / profile -----
    def change_password(self, account):
        if not self.confirm_password(account, "Current password: "):
            return
        new = self.ask_new_password()
        if account.check_password(new):
            print("❌ New password must be different from the current one.")
            return
        account.set_password(new)
        self.bank.save()
        print("✅ Password changed successfully.")

    def profile_menu(self, account):
        while True:
            print(f"""
        --- Profile ---
        Name           : {account.fullname}
        Email          : {account.email}
        Phone          : {account.phone}
        Account number : {account.account_number}
        Account type   : {account.account_type}
        Member since   : {account.created_at}

        1. Update full name
        2. Update email
        3. Update phone number
        4. Change security question
        #. Back
            """)
            choice = input("Choice: ").strip()
            if choice == "1":
                name = input("New full name: ").strip().title()
                if not name:
                    print("❌ Name can't be empty.")
                    continue
                account.fullname = name
            elif choice == "2":
                email = input("New email: ").strip().lower()
                if not valid_email(email):
                    print("❌ Invalid email address.")
                    continue
                if self.bank.find_by_email(email):
                    print("❌ That email is already in use.")
                    continue
                if not self.confirm_password(account):
                    continue
                account.email = email
            elif choice == "3":
                phone = input("New phone number: ").strip()
                if not valid_phone(phone):
                    print("❌ Phone number must be 10 to 14 digits.")
                    continue
                account.phone = phone
            elif choice == "4":
                if not self.confirm_password(account):
                    continue
                for i, q in enumerate(SECURITY_QUESTIONS, 1):
                    print(f"  {i}. {q}")
                pick = input("Choice: ").strip()
                if not pick.isdigit() or not 1 <= int(pick) <= len(SECURITY_QUESTIONS):
                    print("❌ Invalid choice.")
                    continue
                answer = input("Answer: ").strip()
                if not answer:
                    print("❌ Answer is required.")
                    continue
                account.security_question = SECURITY_QUESTIONS[int(pick) - 1]
                account.security_answer_hash = hash_secret(answer.lower())
            elif choice == "#":
                return
            else:
                print("Invalid choice.")
                continue
            self.bank.save()
            print("✅ Profile updated.")

    def close_account(self, account):
        print("⚠️  Closing your account is permanent.")
        if account.balance > 0:
            print(f"❌ Withdraw your remaining balance ({money(account.balance)}) first.")
            return False
        if input("Type CLOSE to confirm: ").strip() != "CLOSE":
            print("Cancelled.")
            return False
        if not self.confirm_password(account):
            return False
        self.bank.delete_account(account)
        print("✅ Your account has been closed.")
        return True

    # ----- menus -----
    def account_menu(self, account):
        while True:
            print(f"""
        ===== {account.fullname} | {account.account_number} =====
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance
        5. Transaction history
        6. Account statement
        7. Buy airtime
        8. Profile / account management
        9. Change password
        0. Close account
        #. Logout
            """)
            choice = input("Choice: ").strip()
            if choice == "1":
                self.deposit(account)
            elif choice == "2":
                self.withdraw(account)
            elif choice == "3":
                self.transfer(account)
            elif choice == "4":
                self.check_balance(account)
            elif choice == "5":
                self.transaction_history(account)
            elif choice == "6":
                self.statement(account)
            elif choice == "7":
                self.buy_airtime(account)
            elif choice == "8":
                self.profile_menu(account)
            elif choice == "9":
                self.change_password(account)
            elif choice == "0":
                if self.close_account(account):
                    break
            elif choice == "#":
                print("Signing out...")
                break
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            print("""
        ===== PYBANK =====
        1. Create account
        2. Login
        3. Reset password
        #. Exit
            """)
            choice = input("Choice: ").strip()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.reset_password()
            elif choice == "#":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    try:
        BankApp().run()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
