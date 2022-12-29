from encrypt import encrypt
from decrypt import decrypt
import os
import time
import sys


def get_user_mode_key() -> tuple[int, int]:
    """ The user tells the program with he wants to crypt a message or decrypt a message using a key """

    # Palette
    underline = '\x1b[4m'
    reset = '\x1b[0m'

    # Check what wants the user, either encrypt a message, either decrypt it
    mode = int(input(f"""Do you want to {underline}encrypt{reset} or to {underline}decrypt{reset}:
1.  ENCRYPT
2.  DECRYPT
    \n"""))
    while mode not in [1, 2]:
        mode = int(input(f"Please choose between option {underline}1{reset} and {underline}2{reset}.\n"))

    # Get the key of the user
    os.system('cls')
    key = int(input("Enter the key (1-25): "))
    while mode < 1 or mode > 25:
        key = int(input("You must enter a number between 1 and 25: "))
    return mode, key


def get_string():
    """ Gets the message of the user """

    os.system('cls')
    string = str(input("Enter the text you want to encrypt:\n"))
    return string


def print_result(converted_string, mode, key):
    """ Prints the encrypted or decrypted message """
    os.system('cls')
    text = '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'
    for element in text:
        sys.stdout.write(element)
        sys.stdout.flush()
        time.sleep(.005)
    print("\n")

    # Palette
    underline = '\x1b[4m'
    reset = '\x1b[0m'

    os.system('cls')
    if mode == 1:
        print(f"""Your encrypted message is:\n
{converted_string}

{underline}The key is {key}.{reset}\n""")
        input("Press Enter ton continue...")
    elif mode == 2:
        print(f"""Your decrypted message is:\n
{converted_string}\n""")
        input("Press Enter ton continue...")


def main():
    mode, key = get_user_mode_key()
    string = get_string()
    if mode == 1:
        converted_string = encrypt(string, key)
        print_result(converted_string, mode, key)
    if mode == 2:
        converted_string = decrypt(string, key)
        print_result(converted_string, mode, key)


if __name__ == '__main__':
    main()
