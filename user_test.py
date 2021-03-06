import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Makena", "Makena99*")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.login_username, "Makena")
        self.assertEqual(self.new_user.login_password, "Makena99*")

    def test_save_user(self):
        '''
        test case to test if the user object is saved in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
