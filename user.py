class User:
    '''
    Class that generates new instances of users.
    '''

    def __init__(self, name, email, login_username, login_password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: User's first name
            last_name: User's last name
            email: User's email
            username: login user name
            password: login password
        '''
        self.name = name
        self.email = email
        self.login_username = login_username
        self.login_password = login_password
