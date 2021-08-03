class User:
    """
    Class that generates new instances of users
    """

    user_list = [] # Empty contact list

    def __init__(self,first_name, last_name, user_name, password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New users first name.
            last_name : New users last name.
            user_name: New users username.
            password : New users password.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
