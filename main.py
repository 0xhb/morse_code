from re import M


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    encrypted_message = ''
    for letter in message:
        for key in MORSE_CODE_DICT:
            if letter == key.lower():
                encrypted_message += f"{MORSE_CODE_DICT[key]} "
    return encrypted_message

def decryption(message):
    decrypted_message = ''
    for item in message.split():
        for letter in  MORSE_CODE_DICT:
            if item == MORSE_CODE_DICT[letter]:
                decrypted_message += f"{letter} "

    return decrypted_message

choice = input("Enter E for encryption and D for decryption or q to quit: ")
while choice.lower() != "q":
    msg = input("Enter your message: ")
    if choice.lower() == "e":
        print(encrypt(msg))
    elif choice.lower() == "d":
        print(decryption(msg))
    choice = input("Enter E for encryption and D for decryption or q to quit: ")