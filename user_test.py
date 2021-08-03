import unittest # Importing the unittest module
from user import Account, User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gagan", "Chhabra", "gsgagan", "password1234")

    def test_init(self):
        '''
        test_init test case to see if object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name, "Gagan")
        self.assertEqual(self.new_user.last_name, "Chhabra")
        self.assertEqual(self.new_user.user_name, "gsgagan")
        self.assertEqual(self.new_user.password, "password1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving the new user_list
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_save_multiple_users(self):

        '''
        Check if we can save multiple user objects to our user_list
        '''
        
        self.new_user.save_user()
        test_user = User("Luke", "Skywalker", "darthvader", "iamyourfather")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we van remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Tony", "Stark", "ironman", "wedidit")
        test_user.save_user()

        self.new_user.delete_user() #Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display infformation
        '''

        self.new_user.save_user()
        test_user = User("Tony", "Stark", "ironman", "wedidit")
        test_user.save_user()

        found_user = User.find_by_username("ironman")
        self.assertEqual(found_user.user_name,"ironman")

    def test_display_user_information(self):
        '''
        test to check if we can be able to display users saved in user_list
        '''

        self.assertEqual(User.display_userInfo(),User.user_list)

class TestAccount(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Twitter", "gsgagan", "password1234")