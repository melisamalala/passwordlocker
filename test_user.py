#!/usr/bin/env python3.6

# import unittest
# from user import User
#
#
# def test_create_User(first_name,last_name,password):
#     '''
#     This is a function to create a new user
#     '''
#     new_user = User(first_name,last_name,password)
#     return new_user
#
#
# # def save_user
#

import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

        # setting up here

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

        # other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user list
            '''
            self.new_user.save_user()
            test_user = User("Test", "user", "moringa")  # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list), 2)

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Melissa","Malala","moringa") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Melissa")
        self.assertEqual(self.new_user.last_name,"Malala")
        self.assertEqual(self.new_user.password, "moringa")

    # def test_create_User(first_name, last_name, password):
    #
    #
    #     '''
    #     This is a function to create a new user
    #     '''
    #     new_user = User(first_name,last_name,password)
    #     return new_user

    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)

    # def test_save_multiple_user(self):
    #     '''
    #     test_save_multiple_user to check if we can save multiple user
    #     objects to our user list
    #     '''
    #     self.new_user.save_user()
    #     test_user = User("Test", "user", "moringa")  # new contact
    #     test_user.save_user()
    #     self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()