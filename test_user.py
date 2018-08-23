#!/usr/bin/env python3.6

import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

        # setting up here

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Melissa","Malala","moringa") # create user object


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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Melissa")
        self.assertEqual(self.new_user.last_name,"Malala")
        self.assertEqual(self.new_user.password, "moringa")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "moringa")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)



if __name__ == '__main__':
    unittest.main()