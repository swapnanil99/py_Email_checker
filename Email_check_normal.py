email = input("Enter your Email: ")
if len(email) >=6 :
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            pass
        else:
            print("Invalid Email 3")
    else:
        print("Invalid Email 2")
else:
    print("Invalid Email 1")
print("Valid Email")
    