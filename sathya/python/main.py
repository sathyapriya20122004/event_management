# main.py

import login
import calculator

def main():
    """Main function to handle login and calculator operations."""
    if login.authenticate_user():
        print("Login successful!")
        calculator.calculator()
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
