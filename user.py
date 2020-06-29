class User:
    '''
    Class that generates new instances of users.
    '''

    def __init__(self, first_name, last_name, email, login_username, login_password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: User's first name
            last_name: User's last name
            email: User's email
            username: login user name
            password: login password
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_username = login_username
        self.login_password = login_password
