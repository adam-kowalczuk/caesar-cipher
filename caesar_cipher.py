alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    # Loop through each letter of plain_text input
    for letter in plain_text:
        # Get shifted index of each letter
        index = alphabet.index(letter) + shift_amount
        # Add letter at shifted index to cipher_text
        cipher_text += alphabet[index]

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    # Loop through each letter of the cipher_text input
    for letter in cipher_text:
        # Get shifted index of each letter
        index = alphabet.index(letter) - shift_amount
        # Add letter at shifted index to plain_text
        plain_text += alphabet[index]
    print(f"The decoded text is {plain_text}.")


# Check whether user wants to 'encode' or 'decode' message, then call appropriate function
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)
