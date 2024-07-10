# TODO: Create a class that will define the login service (logic of login)
#   - create a function login that take a dict in parameter containing username and password
#   - The login function should call the login_repository (or user_repository as you prefer) to find the user that match the same username
#   - Given the user create the password and check if it match the one sotred in database
#     - if yes -> generate the token using the `my_jwt.py` module
#     - else -> returns an error 401, with message "wrong credentials" /!\