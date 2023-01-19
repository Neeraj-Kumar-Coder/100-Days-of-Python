# Algorithm Used:

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

import string
import random

# Variables used
message = ""
cipher_text = ""


# Encryption
message = input("Enter your message to encrypt: ")
length_of_message = len(message)

if (length_of_message < 3):
    cipher_text = message[::-1]  # Reversing the string
else:
    cipher_text = message[1:] + message[0]
    cipher_text = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + random.choice(string.ascii_letters) + cipher_text
    cipher_text += random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + random.choice(string.ascii_letters)

print(f"The Encrypted message is = {cipher_text}")


# Decryption
cipher_text = input("Enter the encrypted message: ")
length_of_message = len(cipher_text)

if (length_of_message < 3):
    message = cipher_text[::-1]
else:
    message = cipher_text[3:length_of_message - 3]
    message = message[length_of_message - 7] + message[0:length_of_message - 7]

print(f"The message is = {message}")
