# Substitution cipher program that shifts letters in a string by a given key

plain_string = "ZEBRA CROSSING"  # The original text to be encrypted
key = 3  # Number of positions each letter in the string will be shifted
conv = 0  # Variable to store the converted ASCII value of each character

# Loop through each character in the plain_string
for x in range(len(plain_string)):
    # Convert the current character to ASCII, add the key, and store in conv
    conv = ord(plain_string[x]) + key

    # Check if the new ASCII value goes beyond 'Z' (90 in ASCII)
    if conv > 90:
        # If so, wrap around by subtracting 26 to stay within uppercase alphabet range
        print(chr(conv - 26))
    # Check if the character is a space (ASCII 32), which shifts to ASCII 35 + key
    elif conv == 35:
        # Convert it back to a space and print
        print(chr(32))
    else:
        # If the character is within 'A' to 'Z' range, print the shifted character
        print(chr(conv))
