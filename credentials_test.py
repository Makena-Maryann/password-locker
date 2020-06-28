import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter", "Makena", "Maryann99")

    def test_init(self):
        '''
        test_init test case to test if if the object is initialized properly.
        '''
        self.assertEqual(self.new_credentials.account_name, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "Makena")
        self.assertEqual(self.new_credentials.password, "Maryann99")


if __name__ == '__main__':
    unittest.main()
