import re
email_condition = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #Regular expression for validating an Email
user_email = input("Enter your Email: ")
if re.search(email_condition, user_email):
    print("Valid Email")
else:
    print("Invalid Email")
    exit(1)
