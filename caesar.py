

import string
def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_lower = letter.lower()
    letter_index = alphabet.find(letter_lower)
    return (letter_index)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_position =alphabet_position(char)
    if char_position != -1:
                newChar =alphabet[(char_position+rot)%26]
                if char in string.ascii_uppercase:
                    return newChar.upper()
                else:
                    return newChar
    else:
                return (char)
def encrypt(text, rot):
    newText = ""
    for lettr in text:
        newText += rotate_character(lettr, rot)

    return newText
