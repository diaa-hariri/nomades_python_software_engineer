"""
This is a hashed password that is generated using the SHA-256 algorithm.
You task is to find the password that was used to generate this hash.
For that you need to know some information about the password:
- It is an alphabetical string
- It is a lower case string
- It is a 5 letter string

The password to be found is hashed using the SHA-256 algorithm.
The SHA-256 algorithm is a hashing algorithm that takes a string as input and generates a 256 bit (32 byte) hash as output.
The hash is a hexadecimal string that is 64 characters long.
You can use the hashlib library to generate the hash of a string.
example:
    ```python
    password = hashlib.sha256("MyCurrentPassword".encode()).hexdigest()
    ```

Knowing that information, 
you can write a program that will generate all possible combinations of 5 letter strings. and try to break the password.
"""

import hashlib
import string
import time
import random
# install tqdm library using:
#   conda install tqdm
from tqdm import tqdm

def brute_force_password(charset, length, target_hash):
    import itertools
    MAX_ITER = len(charset) ** length
    start_time = time.time()

    # for char1 in charset:           # -> n (n=>len(charset)=>26)
    #   for char2 in charset:         # -> n*n
    #     for char3 in charset:       # -> n*n*n = n^3
    #       for char4 in charset:     # -> n^4
    #         for char5 in charset:   # -> n^5

    #             p = char1+char2+char3+char4+char5
    #             password = hashlib.sha256(p.encode()).hexdigest()
    #             if password == target_hash:
    #                 return p, time.time() - start_time

    # for p in itertools.product(charset, repeat=length):
    #   p = "".join(p)
    #   password = hashlib.sha256(p.encode()).hexdigest()
    #   if password == target_hash:
    #     return p, time.time() - start_time 

    # return None, time.time() - start_time

    # p = "aaaaa" # -> 00000 -> 0
    # p = "aaaab" # -> 00001 -> 1
    # p = "aaaaz" # -> 0000[25] -> 25
    # p = "aaaba" # -> 0000[25] -> 26
    for i in tqdm(range(MAX_ITER)):
      p = ""
      for j in range(length-1, -1, -1):
          p += charset[i // (len(charset)**j) % len(charset)]
      password = hashlib.sha256(p.encode()).hexdigest()
      if password == target_hash:
        return p, time.time() - start_time
    
    return None, time.time() - start_time

# Example usage:
charset = string.ascii_lowercase  # Define your character set
length = 5  # Define the length of the password
target_hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

password, time_taken = brute_force_password(charset, length, target_hash)

if password:
    print("Password:", password)
    print("Time taken:", time_taken)
else:
    print("Password not found.")

"""
Questions Part
1. What is the time complexity of the brute force algorithm?


2. What would be the time complexity if the password was 6 characters long instead of 5?


3. What would be the value of MAX_ITER if the password contains uppercase letters, lowercase letters, digits and special characters?


4. Imagine you have a computer that clock a 4GHZ (4 billion cycles per second). 
  Complete the table below with the time taken to break the password for different lengths of passwords.
  ```
  | population/length | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
  |-------------------|---|---|---|---|---|----|----|----|----|----|
  | lower_case (26)   | | | | | | | | | | |
  | upper_case (26)   | | | | | | | | | | |
  | digits (10)       | | | | | | | | | | |
  | special (32)      | | | | | | | | | | |
  | alpha_lower_upper (52) | | | | | | | | | | |
  | alphanumeric (62) | | | | | | | | | | |
  | all_characters (95) | | | | | | | | | | |
  ```
"""
