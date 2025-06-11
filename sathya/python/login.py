import calculator 

def user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "sa" and password == "vi":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

if user():
    calculator.main()