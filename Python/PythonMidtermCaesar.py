# Description: Caesar Cipher problem
# Author: Stephen Fennelly
# Dates: 2025-02-18


# Define required libraries



# Define constants




# Define program functions

def Caesar_Cipher(text, shift):                                                     # defines caesar_cipher as the inputs
    result = ""                                                                     # empty string to where the encrypted text is stored
    for char in text:
        if char.isalpha():                                                          # checks if the text is letters
            shift_start = ord('A') if char.isupper() else ord('a')                  # ord('A') is the ASCII value for A while ord('a') is the ASCII value for a, doing this check shifts upper and lower case letters separately
            result += chr(shift_start + (ord(char) - shift_start + shift) % 26)     # ord(char) - shift_start converts the letter into a 0-based index (e.g., 'A' = 0, 'B' = 1), +shift moves the character by the shift amount
        else:                                                                       # % 26 ensures the program loops if Z/z is reached (26th letter), chr(shift_start + (..)) converts it back to ASCII and chr(..) converts back to characters
            result += char                                                          # anything not a letter will be added to result without being changed

    return result 

# Main program starts here

# Gather user inputs

while True:
    Msg = input("Enter a message you would like to encrypt or decrypt: ")
    Shift = int(input("Enter a value for the characters to be shifted (e.g., 3): "))

    Mode = input("Type 'encrypt' to encode or 'decrypt' to decode: ").strip().lower()

    if not Mode.isalpha():
        print()
        print("Please enter 'encrypt' or 'decrypt' only.")
        continue

    # Perform required calculations and display results

    if Mode == "encrypt":
        encrypted_message = Caesar_Cipher(Msg, Shift)
        print("Encrypted message:", encrypted_message)
    elif Mode == "decrypt":
        decrypted_message = Caesar_Cipher(Msg, -Shift)                                  # -Shift reverses the calculation
        print("Decrypted message:", decrypted_message)
    else:
        print("Please enter 'encrypt' or 'decrypt'.")
        continue

    Continue = input("Would you like to encrypt/decrypt another message? (yes/no): ").strip().lower()
    if Continue != "yes":
        print("Thank you for using this encryption program!")
        break

# Write the values to a data file for starage

# Any housekeeping duties at the end of the program