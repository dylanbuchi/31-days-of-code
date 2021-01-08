# Caesar Cipher
import sys
import os

# add this to import the logo and run the file here
sys.path.append(os.getcwd())

from src.day_8.logo import LOGO

# Global constant variable
ALPHABET = [chr(i) for i in range(97, 123)]


def run_again():
    choice = input("Press enter to run again")
    if not choice:
        main()


def ask_user_encryption_details():
    text = space = ' '
    shift = 5

    while True:
        try:
            text = input("Type your message:\n").lower()
            assert text.isalpha() or space in text
            shift = int(input("Type the shift number:\n"))

        except (ValueError, AssertionError):
            print("Error, please try again with valid inputs")
            continue
        else:
            return text, shift


def choose_codec_mode(mode, text: str, shift):
    parts = []

    for ch in text:
        if not ch.isalpha():
            parts.append(ch)

        else:
            index = (ALPHABET.index(ch))
            index = index + shift if mode == 'encode' else index - shift
            parts.append(ALPHABET[index % 26])

    return ''.join(parts)


def run_caesar_cipher(text, shift, mode):
    return choose_codec_mode(mode, text, shift)


def user_interface():
    mode = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n"
                 ).lower().strip()
    text, shift = ask_user_encryption_details()
    result = run_caesar_cipher(text, shift, mode)

    print(f"The {mode}d message is: {result}")


def main():
    print(LOGO)
    try:
        user_interface()
        run_again()

    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()