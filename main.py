from art import logo

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


def caesar(direction, text, shift):
    output = ""
    # If cipher direction is "decode", multiply shift amount by -1 so that shift happens to the left
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            output += alphabet[new_position]
        # If character is not a letter, simply append it to the output (no encoding necessary)
        else:
            output += char
    print(f"The {direction}d text is {output}.")


# Print 'Caesar Cipher' logo
print(logo)

# Prompt user for cipher direction, text to encode/decode, and shift amount
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
# The '% 26' accounts for whether the supplied shift amount is greater than 26
shift = int(input("Type the shift number:\n")) % 26

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

caesar(direction, text, shift)
