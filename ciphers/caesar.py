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
    
    
