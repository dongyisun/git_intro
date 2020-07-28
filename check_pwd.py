def check_pwd(pwd):
    accepted_symbols = ["~", "`", "!", "@", "#", "$", "%", "^",
                        "&", "*", "(", ")", "_", "+", "-", "="]
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    elif not any(map(str.islower, pwd)):
        return False
    elif not any(map(str.isupper, pwd)):
        return False
    elif not any(map(str.isdigit, pwd)):
        return False
    elif not any(symbol in pwd for symbol in accepted_symbols):
        return False
    return True
