class User:
    '''
    Class that generates new instances of users.
    '''

    user_list = []

    def __init__(self, login_username, login_password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            login_username: new user login user name
            login_password: new user login password
        '''

        self.login_username = login_username
        self.login_password = login_password

    def save_user(self):
        '''
        Method to save the user objects into the user_list
        '''

        User.user_list.append(self)
