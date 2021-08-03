import unittest # Importing the unittest module
from user import User # Importing the contact class

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