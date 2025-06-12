# String manipulation

# Initialize a string to be encrypted
plain_string = "HELLO WORLD"  # The variable 'plain_string' holds the string "HELLO WORLD"
key = 3                        # The key for the Caesar cipher (number of positions to shift)
conv = 0                       # Initialize a variable 'conv' to hold the converted ASCII value

# Loop through each character in the 'plain_string'
for x in range(len(plain_string)):  # Iterate over the length of the string
    # Convert the character at index 'x' to its ASCII value, add the key to shift it
    conv = ord(plain_string[x]) + key  # 'ord()' returns the ASCII value, and 'key' is added to it

    # Print the character that corresponds to the new ASCII value after shifting
    print(chr(conv))  # 'chr()' converts the modified ASCII value back to a character and prints it
