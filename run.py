#!/usr/bin/env python3.6
from password import Password
from user import User
import random


'''
User Information
'''


def create_user(first_name, last_name, password):
    """
    Function to create a new user_list
    """
    new_user = User(first_name, last_name, password)
    return new_user

# Save users


def save_users(user):
    """
    Function to save user
    """
    user.save_user()


# Delete user


def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


# Finding a user


def find_user(number):
    """
    Function that finds a user by number and returns the contact
    """
    return User.find_by_number(number)

# Check if a contract exists


def check_existing_user(number):
    """
    Function that checks if a user exists with that number and return Boolean
    """
    return User.user_exist(number)

# Displaying all users


def display_users():
    """
    Function that returns all the save users
    """
    return User.display_users()

# Copy pasting


def copy_password(number):
    """
    Function that copys to machines clipboard
    """
    return User.copy_password()



"""
Accounts and Passwords
"""


def create_profile(account_name, account_password, password_length):
    """
    Function to create new_profile
    """
    new_profile = Password(account_name, account_password, password_length)
    return new_profile


def save_profile(profile):
    """
    Function to save profile
    """
    profile.save_profile()


def find_profile(account_name):
    """
    Function finds password by account name and returns full details
    """
    return Password.find_by_account(account_name)


def profile_exists(account_name):
    """
    Function that check if a profile exists using an account name to return a
    boolean if it is found or not.
    """
    return Password.profile_exists(account_name)


def display_profiles():
    """
    Function that returns all save profiles
    """
    return Password.display_profiles()


def copy_password(account_name):
    """
    Function that allows us to copy a password from matching account_name
    """
    return Password.copy_password()


def password_gen(password_length):
    return Password.password_gen(password_length)


def main():
    print("Welcome aboard! Everyone has a name so what is yours?")
    user_name = input()
    print("")

    print(f"Hi {user_name}. So ummm.... What would you like to do?")
    print("")

    while True:
        print("""Use these short codes:
              createnew - I wanna create a new account
              login - Just wanna login to see my password profiles
              logout - I'm done, log me out please!
              exit - Gotta leave, so lets exit""")
        short_code = input().lower()
        print("_" * 100)
        if short_code == "createnew":
            print("New Password Locker Account")
            print("_" * 20)

            print("Enter your first name -")
            f_name = input()

            print("Enter your last name -")
            l_name = input()

            print("""
                  Did you know that we can generate a strong password for you? Use:
                  g- to generate a password
                  m- to set your own.
                  """)
            pass_code = input().lower()
            print("__" * 20)
            if pass_code == "g":
                password_length = int(
                    input("How long do you want your password - "))
                password = password_gen(password_length)
                print(f"Your new password is {password}")
            else:
                print("We dislike hackers too, so it might be better if you write a password of your own.")
                password = input()

            save_users(create_user(f_name, l_name, password))

            print("")
            print(
                f"""New account created for - {first_name} {last_name} your account password is - {password}""")
            print("")
            print("Feel free to create your password profiles")
        while True:
            print("""Use these short codes:
                  newpassword - create password profile,
                  displaypassword - display password locker profiles,
                  findpassword - find a password profile,
                  exit - exit profile list.""")
            short_code = input().lower()
            print("_" * 100)
            if short_code == "newpassword":
                print(
                    "Quick question, which account do you want to save a password for? Eg Yahoo, Snapchat, Instagram")
                account_name = input()
                print("""
                      By the way... We can create a strong password for you. Use:
                      generatepassword- to generate a password
                      makepassword- to set your own.
                      """)
                pass_code = input().lower()
                print("__" * 20)
                if pass_code == "generate":

                    password_length = int(
                        input("Quick question, how long do you want your password to be? - "))

                    password = password_gen(password_length)
                    print("")
                    print(f"Super, your password for {account_name} is: {password}")
                    print("")
                    print("__" * 20)
                else:
                    print("Cool, please write a password of your own and we will store it (safely, of course) for you")
                    password = input()
                    password_length = len(password)
                    print("")
                    print(f"Super, your password for {account_name} is: {password}")
                    print("")
                    print("__" * 20)

                save_profile(create_profile(
                    account_name, password, password_length))

            elif short_code == "displaypassword":
                if display_profiles():
                    print("Yay, now here is a list of all your profiles")
                    print("")
                    for profile in display_profiles():
                        print(
                            f"Account- {profile.account_name}, Password- {profile.password}, Password Length- {profile.password_length}")
                        print("")
                else:
                    print("")
                    print("Sorry, but you don't seem to have any profiles saved yet")
                    print("")

            elif short_code == "findpassword":
                print("Please enter the account you want to find the password for")

                account_name = input()
                if profile_exists(account_name):
                    search_profile = find_profile(account_name)
                    print("_" * 20)
                    print(f"{search_profile.account_name}")
                    print(f"Password - {search_profile.password}")
                    print("")
                    print(
                        f"Password Length - {search_profile.password_length}")
                    print("_" * 20)
                else:
                    print("That profile does not exist")
                    print("")

            elif short_code == "exit":
                print("")
                print(
                    "*" * 10 + " Aww, thank you for visiting Password Locker. " + "*" * 10)
                print("")
                break


if __name__ == '__main__':
    main()
