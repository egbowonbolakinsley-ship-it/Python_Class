import re

def validate_email(email):
    # pattern = r"^\w+@\w+\.\w+$"
    pattern = r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$"
    match = re.match(pattern, email)
    # print(match)
    if match:
        print(f"{email} is a valid mail")
    else:
        print(f"{email} is not a valid mail")
        

email = input("Email: ")        
# validate_email(email)