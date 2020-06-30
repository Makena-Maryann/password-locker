#!/usr/bin/env python3.6
from user import User
from credentials import Credentials


def main():
    print("Hello, Welcome to your password locker.")

    print("What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : lg - login into your account, su - sign up, ex - exit the password locker")

        short_code = input().lower()
        if short_code == 'lg':
            print("Enter Username .....")
            lg_username = input()

            print("Enter Password .....")
            lg_password = input()

# Validate the password and username inputted is correct. If so, call the credentials function. If not, print("Wrong username or password. Please try again.")

# If sign up username and password = login username and password, execute credentilas fxn.
# else, print("Wrong username or password. Please try again.")
        elif short_code == "su":
            print("Create an account")
            print("-"*10)

            print("Full name ....")
            f_name = input()

            print("Email address ....")
            e_address = input()

            print("Username ....")
            u_name = input()

            print("Password ....")
            p_word = input()

# Create user instance and save it for use in the login.
            print("Account created successfully!")
# Initiate login
        elif short_code == "ex":
            print("Bye ......")
            break
        else:
            print("Wrong short code. Please try again.")


if __name__ == '__main__':

    main()
