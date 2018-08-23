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

        Args:
            Account Name: This is the account name to search for, e.g social media sites Gmail, Yahoo, Twitter, Facebook.
        Returns :
            Password of the person that matches the account name.
        '''

        for user in cls.user_list:
            if user.password == account_name:
                return user
#
#     @classmethod
#     def contact_exist(cls, number):
#         '''
#         Method that checks if a contact exists from the contact list.
#         Args:
#             number: Phone number to search if it exists
#         Returns :
#             Boolean: True or false depending if the contact exists
#         '''
#         for contact in cls.contact_list:
#             if contact.phone_number == number:
#                 return True
#
#         return False
#
#     def display_contacts(cls):
#         '''
#         method that returns the contact list
#         '''
#         return cls.contact_list
#
#
# def test_copy_email(self):
#     '''
#     Test to confirm that we are copying the email address from a found contact
#     '''
#
#     self.new_contact.save_contact()
#     Contact.copy_email("0712345678")
#
#     self.assertEqual(self.new_contact.email, pyperclip.paste())
#
#
# def copy_email(cls, number):
#     contact_found = Contact.find_by_number(number)
#     pyperclip.copy(contact_found.email)
