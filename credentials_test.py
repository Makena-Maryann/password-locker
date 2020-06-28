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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if if the object is initialized properly.
        '''
        self.assertEqual(self.new_credentials.account_name, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "Makena")
        self.assertEqual(self.new_credentials.password, "Maryann99")

    def test_save_credentials(self):
        '''
        Test case to test if the credentials object is saved in the credentials list.
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials objects to the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test", "user", "make254*")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test to check if we can delete credentials 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test", "user", "make254*")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
