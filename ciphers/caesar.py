# define the English alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
from utils import alphabet, process_plaintext

# if plaintext is all lowercase, convert to uppercase
# Remove all non-alphabet characters from the plaintext
# return processed plaintext
def process_plaintext(plaintext):
    processed = ""
    plaintext = plaintext.upper()

    for char in plaintext:
        if char in alphabet:
            processed += char

    return processed


def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    processed_plaintext = process_plaintext(plaintext)

    # create an empty list that contains the mappings from the alphabet to its corresponding number
    encrypted_text = []

    for val in processed_plaintext:
        num = alphabet.index(val)
        num = num  + shift
        encrypted_num = num % 26
        encrypted_val = alphabet[encrypted_num]
        encrypted_text.append(encrypted_val)
    result = "".join(encrypted_text)    
    return result   

    

if __name__ == "__main__":
    user_plaintext = input("Input your plaintext: ")

    # While loop to ensure proper input validation, catch errors when trying to conver to int
    while True:
        user_shift = input("Input your key (shift): ")
        try:
            user_shift = int(user_shift)
            break # if valid, exit loop
        except ValueError:
            print("Input is not an integer, try again\n")

    print(encrypt_caesar(user_plaintext, user_shift))
    
    
