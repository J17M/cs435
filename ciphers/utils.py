# define the English alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
