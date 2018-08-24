
import pyperclip
import random


'''
Define the class that will build the password manager, and then create different accounts that need a password and the passwords generated by the app or that the user selects for themselves
'''

class User:
    def __init__(self, first_name, last_name, profile_key):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_key = profile_key

class Password:
    password_list = []


    def __init__(self,account_name,password,password_length):

      # docstring removed for simplicity

        self.account_name = account_name
        self.password = password
        self.password_length = password_length


    def save_profile(self):
        """
        Here we build our save profile function that will append every account
        and password profile.
        When we import it and use it on our test_save profile test-case...it
        should work.
        """
        Password.password_list.append(self)

    @classmethod
    def profile_exists(Password, account_name):
        """
        Method checks if a profile exists from password_list. It takes in the
        name and returns a boolean if it finds a matching account.
        """
        for profile in Password.password_list:
            if profile.account_name == account_name:
                return True
        return False

    @classmethod
    def display_profiles(Password):
        """
        Method that will return profile list.
        """
        return Password.password_list

    @classmethod
    def find_by_account(Password, account_name):
        """
        This method takes in an account name and returns the password matching
        the account.
        """
        for profile in Password.password_list:
            if profile.account_name == account_name:
                return profile

    @classmethod
    def copy_password(Password, account_name):
        password_found = Password.find_by_account(account_name)
        pyperclip.copy(password_found.account_password)

    @classmethod
    def password_gen(Password, password_length):
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$^&*()`'
        password = "".join(random.sample(string, int(password_length)))
        account_passsword = password
        return account_passsword



