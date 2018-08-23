def create_profile(account_name, password, password_length):
    """
    Function to create new_profile
    """
    new_profile = Password(account_name, password, password_length)
    return new_profile


def save_profile(profile):
    """
    Function to save profile
    """
    profile.save_profile()


def find_profile(account_name):
    """
    Function finds password by account name and returns full details
    """
    return Password.find_by_account(account_name)


def display_profiles():
    """
    Function returns all the save profiles
    """
    return Password.display_profiles()
