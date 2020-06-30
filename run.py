#!/usr/bin/env python3.6
from user import User
from credentials import Credentials


def create_user(lg_name, lg_passcode):
    '''
    Function to create a new user
    '''
    new_user = User(lg_name, lg_passcode)
    return new_user


def save_new_user(user):
    '''
    Function to save new user
    '''
    user.save_user()


def create_credential(aname, uname, password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(aname, uname, password)
    return new_credentials


def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credentials()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credentials()


def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def creds_list():
    print("What would you like to do?")
    print('\n')

    while True:
        print("Please use these codes to state what you want: cc - create a new credential, dc - display all the available credentials, del - delete a credential, ex - exit the credentials list")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print("Account name ....")
            a_name = input()

            print("Username ....")
            u_name = input()

            print("Password ....")
            passcode = input()

            save_credential(create_credential(a_name, u_name, passcode))
            print('\n')
            print(f"{a_name} account credentials saved")
            print("\n")

        elif short_code == 'dc':
            if display_credential():
                print("Here is a list of all your credentials")
                print('\n')

                for credential in display_credential():
                    print(
                        f"{credential.account_name} {credential.user_name} {credential.password}")

                    print('\n')

            else:
                print('\n')
                print("You don't seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'del':
            print("Enter the name of the account you want to delete.")

            delete_account = input()

            del_credential(delete_account)

        elif short_code == "ex":
            print("Bye ........")
            break

        else:
            print("Wrong short code. Please try again.")


def main():
    print("Hello, Welcome to your password locker.")

    print("What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : lg - login into your account, su - sign up, ex - exit the password locker")

        short_code = input().lower()

        if short_code == "su":
            print("Create an account")
            print("-"*10)

            print("Username ....")
            u_name = input()

            print("Password ....")
            p_word = input()

            save_new_user(create_user(u_name, p_word))
            print('\n')
            print(f"Congratulations {u_name}. Account created successfully!")
            print('\n')
            print("Please login....")
            print("Enter Username .....")
            lg_username = input()

            print("Enter Password .....")
            lg_password = input()

            if u_name != lg_username or p_word != lg_password:
                print("Invalid username or password!")
                print("Enter Username .....")
                lg_username = input()

                print("Enter Password .....")
                lg_password = input()

            else:
                print('\n')
                print(
                    f"Hi {lg_username}, Welcome to your password locker account.")
                print('\n')
                creds_list()

        elif short_code == 'lg':
            print("Enter Username .....")
            sample_user = input()

            print("Enter Password .....")
            sample_password = input()

            if sample_user != 'newuser' or sample_password != 'pass254':
                print("Account does not exist.Please create an account to login.")

            else:
                print("Hi, Welcome to your password locker account.")
                creds_list()

        elif short_code == "ex":
            print("Bye ......")
            break
        else:
            print("Wrong short code. Please try again.")


if __name__ == '__main__':

    main()
