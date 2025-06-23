class UserNotFoundException(Exception):
    detail = 'User Not Found'

class UserNotCorrectPasswordException(Exception):
    detail = 'User not correct password'