from utils import alphabet


def encrypt_caesar(plaintext, shift):
    # create an empty list that contains the mappings from the alphabet to its corresponding number
    encrypted_text = []
    for char in plaintext:
        # check to see if char is an alphabet character
        if char.isalpha():
            # check case of char
            charUpper = char.isupper()
            indexChar = alphabet.index(char.upper())
            shiftedText = alphabet[(indexChar + shift) % 26]
            encrypted_text.append(shiftedText if charUpper else shiftedText.lower())
        else:
            encrypted_text.append(char) # keep everything that isnt the alphabet    
    return "".join(encrypted_text)   


def decrypt_caesar(ciphertext, shift):
    decrypted_text = []

    for char in ciphertext:
        if char.isalpha():
            charUpper  = char.isupper()
            indexChar = alphabet.index(char.upper())
            shiftedText = alphabet[(indexChar - shift) % 26]
            decrypted_text.append(shiftedText if charUpper else shiftedText.lower())
        else:
            decrypted_text.append(char)
    return "".join(decrypted_text)

if __name__ == "__main__":
    while True:
        mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
        if mode == "e":
            user_plaintext = input("Input your plaintext: ")
            # While loop to ensure proper input validation, catch errors when trying to convert to int
            while True:
                user_shift = input("Input your key (shift): ")
                try:
                    user_shift = int(user_shift)
                    break  # if valid, exit loop
                except ValueError:
                    print("Input is not an integer, try again\n")
            print(encrypt_caesar(user_plaintext, user_shift))
            break
        elif mode == "d":
            user_ciphertext = input("Input your ciphertext: ")
            while True:
                user_shift = input("Input your key (shift): ")
                try:
                    user_shift = int(user_shift)
                    break
                except ValueError:
                    print("Input is not an integer, try again\n")
            print(decrypt_caesar(user_ciphertext, user_shift))
            break
        else:
            print("Invalid Mode, enter only 'e' or 'd'\n")
    
    
