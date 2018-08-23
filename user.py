class User:
    """
    This is a class that generates new instances of users.
    """

    user_list = [] # Empty user list that will contain information about the user's first name, last name and their password

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    def save_user(self):
         User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)



    @classmethod
    def display_users(self):
        return User.user_list
