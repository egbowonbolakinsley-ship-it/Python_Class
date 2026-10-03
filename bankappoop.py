class User:
    def __init__(self, fullname, email, password, balance=0.0):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount < 1:
            print("Amount can't be less than #1.")
            return

        self.balance += amount
        print(f"You've deposited #{amount}. Your account balance is #{self.balance}")

    def withdraw(self, amount):
        if amount < 1:
            print("Amount can't be less than #1.")
            return


        if amount > self.balance:
            print("Insufficient funds")
            return

        self.balance -= amount
        print(f"You've withdrawn #{amount}. Your account balance is #{self.balance}")

    def check_balance(self):
        print(f"Your account balance is #{self.balance}")


class Bank:
    def __init__(self):
        self.database = []

    def find_user(self, email):
        for user in self.database:
            if user.email == email:
                return user
        return None

    def create_account(self):
        fullname = input("Fullname: ").strip().title()
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()

        if not fullname or not email or not password or not confirm_password:
            print("❌All fields are required")
            return

        if password != confirm_password:
            print("❌Password doesn't match")
            return

        if self.find_user(email):
            print("❌An account with this email already exists")
            return

        user = User(fullname, email, password)
        self.database.append(user)
        print("Registration successfull")

    def login(self):
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        active_user = self.find_user(email)

        if not active_user or active_user.password != password:
            print("Invalid email or password")
            return

        print("Login successfull")
        self.account_menu(active_user)

    def account_menu(self, active_user):
        while True:
            print("""
            1. Deposit
            2. Withdraw
            3. Check balance
            #. Logout   
            """)

            choice = input("Choice: ").strip()
            if choice == "1":
                amount = float(input("Amount: "))
                active_user.deposit(amount)
            elif choice == "2":
                amount = float(input("Amount: "))
                active_user.withdraw(amount)
            elif choice == "3":
                active_user.check_balance()
            elif choice == "#":
                print("Signing out...")
                break
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            print("""
            1. Create Account
            2. Login
            #. Exit      
            """)

            choice = input("Choice: ").strip()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "#":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    bank = Bank()
    bank.run()