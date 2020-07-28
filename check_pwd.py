import re


def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    elif not re.search("[a-z]", pwd):
        return False
    elif not re.search("[A-Z]", pwd):
        return False
    elif not re.search("[0-9]", pwd):
        return False
    elif not re.search("~`!@#$%^&*()_+-=", pwd):
        return False
    return True