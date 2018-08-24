import pyperclip

class User:
    """
    This is a class that generates new instances of users.
    """

    user_list = [] # Empty user list that will contain information about the user's first name, last name and their password

    def __init__(self,first_name,last_name,password):

      # Defining the object user which will include the first name, last name and the password

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):

        '''

       This method will save the user objects into the user list
        '''

        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)


    @classmethod
    def find_by_first_name(cls, first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exist(cls, first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
            return False

    @classmethod
    def display_users(cls):
        return cls.user_list

    def display_users(self):
        return User.user_list


    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in the account name of a user and returns a password that matches that account name.
        Arguments:
            For the account name, a user must be able to search for passwords stored in their accounts such as  Gmail, Yahoo, Twitter, Facebook.
        Returns :
            Whatever the user inputs, they should be able to see the password of the account that they have searched for.
        '''

        for user in cls.user_list:
            if user.password == account_name:
                return user