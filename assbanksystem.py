database = []


def create_account():
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

    user = {
        "fullname": fullname,
        "email": email,
        "password": password,
        "balance": 0.0
    }
    database.append(user)
    print("Registration successfull")


def find_user(email):
    for user in database:
        if user['email'] == email:
            return user
    return None


def deposit(active_user):
    amount = float(input("Amount: "))
    if amount < 1:
        print("Amount can't be less and #1.")
        return

    active_user['balance'] += amount
    print(f"You've deposited #{amount}. Your account balance is #{active_user['balance']}")


def withdraw(active_user):
    amount = float(input("Amount: "))
    if amount < 1:
        print("Amount can't be less and #1.")
        return

    if amount > active_user['balance']:
        print("Insufficient funds")
        return

    active_user['balance'] -= amount
    print(f"You've withrawn #{amount}. Your account balance is #{active_user['balance']}")


def check_balance(active_user):
    print(f"Your account balance is #{active_user['balance']}")


def account_menu(active_user):
    while True:
        print("""
        1. Deposit
        2. Withdraw
        3. Check balance
        #. Logout   
        """)

        choice = input("Choice: ").strip()
        if choice == "1":
            deposit(active_user)
        elif choice == "2":
            withdraw(active_user)
        elif choice == "3":
            check_balance(active_user)
        elif choice == "#":
            print("Signing out...")
            break
        else:
            print("Invalid choice.")


def login():
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    active_user = find_user(email)

    if not active_user or active_user['password'] != password:
        print("Invalid email or password")
        return

    print("Login successfull")
    account_menu(active_user)


def main():
    while True:
        print("""
        1. Create Account
        2. Login
        #. Exit      
        """)

        choice = input("Choice: ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "#":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()