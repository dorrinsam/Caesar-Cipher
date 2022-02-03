def encrypt(plain_text, number_of_shifts):
    result = ""

    # traverse plaintext
    for i in range(len(plain_text)):
        char = plain_text[i]
        # encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + number_of_shifts - 65) % 26 + 65)
        # encrypt lowercase characters
        else:
            result += chr((ord(char) + number_of_shifts - 97) % 26 + 97)

    return result

# inputs
plain_text = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
number_of_shifts = 23
print("plain text: " + plain_text)
print("number of shifts: " + str(number_of_shifts))
print("cipher text: " + encrypt(plain_text, number_of_shifts))