import unittest  
from credentials import Credentials  


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials = Credentials(
            "junior", "kamau", "123456", "ephraimkamau54@gmail.com")  

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name, "junior")
        self.assertEqual(self.new_credentials.usr_name, "kamau")
        self.assertEqual(self.new_credentials.password, "123456")
        self.assertEqual(self.new_credentials.email, "ephraimkamau54@gmail.com")

    def test_save_credentials(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credentials.save_credentials()  
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
            '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "0745734706", "test@user.com")  
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
            test_delete_account to test if we can remove an account from our account list
            '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "0745734706", "test@user.com")  
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_credentials_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "0711223344", "test@user.com") 
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("Test")

        self.assertEqual(found_credentials.email, test_credentials.email)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "0711223344", "test@user.com")  
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("0711223344")
        self.assertTrue(credentials_exists)


if __name__ == '__main__':
    unittest.main()
