# String manipulation

# Initialize a string to be encrypted
plain_string = "ZEBRA"  # The variable 'plain_string' holds the string "ZEBRA"
key = 3                   # The key for the Caesar cipher (number of positions to shift)
conv = 0                  # Initialize a variable 'conv' to hold the converted ASCII value

# Loop through each character in the 'plain_string'
for x in range(len(plain_string)):  # Iterate over the length of the string
    # Convert the character at index 'x' to its ASCII value and shift it by the key
    conv = ord(plain_string[x]) + key  # 'ord()' returns the ASCII value of the character, adding the key (3) for the shift

    # Check if the new ASCII value exceeds the uppercase 'Z'
    if conv > 90:  # ASCII value for 'Z' is 90
        # If the shifted value exceeds 'Z', wrap around to the start of the alphabet
        print(chr(conv - 26))  # Subtract 26 to wrap around, then convert back to a character with 'chr()' and print it
    else:
        # If the shifted value is within the range of uppercase letters, convert and print it directly
        print(chr(conv))  # Convert back to character and print
