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


def clear_console():
    print("\033c", end="")


# Clear console on program start
clear_console()

# Print 'Caesar Cipher' logo
print(logo)

should_continue = True
while should_continue:
    # Prompt user for cipher direction, text to encode/decode, and shift amount
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    # The '% 26' accounts for whether the supplied shift amount is greater than 26
    shift = int(input("Type the shift number:\n")) % 26

    caesar(direction, text, shift)

    # Prompt user to encode or decode another message. If they answer 'no', break the while-loop and exit the program
    result = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
