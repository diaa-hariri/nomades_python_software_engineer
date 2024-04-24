import random
import string

"""
Write a Python program that genrate a random password.
Your random password need to contains at least:
  - 1 upper char
  - 1 lower char
  - 1 digit
  - 1 special char

Also your password needs to be at least 8 char long
"""
def generate_random_password(length=12):
    # Define the character sets to build the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    set1 = random.choice(lowercase_letters)
    set1 += random.choice(uppercase_letters)
    set1 += random.choice(digits)
    set1 += random.choice(special_chars)

    assert type(set1) == str and len(set1) == 4

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    set2 = random.sample(all_chars, length-4)
    password_lst = list(set1) + set2
    random.shuffle(password_lst) 
    
    # password_str = ""
    # for char in password_lst:
    #     password_str += char
    # return password_str

    return "".join(password_lst)

# Example usage
password = generate_random_password()
print("Random Password:", password)
