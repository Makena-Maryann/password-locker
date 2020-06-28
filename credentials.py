class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = []

    def __init__(self, account_name, user_name, password):
        """
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New credentials account name
            user_name: New credentials user name
            password: New credential password
        """
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        '''
        this method saves credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method deletes saved credentials from the credentials list
        '''
        Credentials.credentials_list.remove(self)
