attempts=0
username="root"
passwd="********"
while attempts<5:
    attempt_u=input("Enter your username")
    attempt_p=input("Enter your password")
    attempts=attempts+1
    if attempt_u==username and attempt_p==passwd:
        print("Welcome")
        break
    elif attempt_u==username and attempt_p!=passwd:
        print("Password incorrect")
    else:
        print("Username or password is incorrect")
if attempts==5:
    print("Access denied")