import random
import string
import openpyxl
def the_ENCRYPT():


    chars = string.punctuation + string.digits + string.ascii_letters + " "
    chars = list(chars)

    keys = chars.copy()
    random.shuffle(keys)

    #ENCRYPT
    plain_text = input("Enter a massege to encypte: ")
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += keys[index]
    print(f"cyphers text: {cipher_text}")

the_ENCRYPT()
