import math
import random

def cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or not
            base = ord("A") if char.isupper() else ord('a')
            # Perform the shift ensuring it wraps around the alphabet
            encrypted += chr((ord(char) - base + shift) % 26 + base) 
        else:
            # Non-letter characters remain unchanged
            encrypted += char
    return encrypted


def cipher_decrypt(encrypted_text, unshift):
    # Decript is simply encryption with the negative of the shift
    return cipher_encrypt(encrypted_text, -unshift)

print(cipher_decrypt("Gjwsfwi", 5))
print(cipher_encrypt("Bernard", 5))

