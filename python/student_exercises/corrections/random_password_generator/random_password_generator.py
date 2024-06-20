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
    if length < 8:
        raise ValueError("Password should be at least 8 chars long")

    # Define the character sets to build the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase_letters+uppercase_letters+digits+special_chars

    password = random.choice(lowercase_letters)\
              +random.choice(uppercase_letters)\
              +random.choice(digits)\
              +random.choice(special_chars)
    remaining_chars = random.sample(all_chars, length-4)
    password = list(password) + remaining_chars

    random.shuffle(password)
    return "".join(password)

# Example usage

password = generate_random_password(3)  
print("Random Password:", password)
