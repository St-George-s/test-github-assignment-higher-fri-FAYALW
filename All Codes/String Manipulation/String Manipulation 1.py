# String manipulation

# Initialize a string variable with the name
myName = "Faye Saif Alwan"  # The variable 'myName' holds the string "Faye Saif Alwan"

# Loop through each character in the string 'myName'
for x in range(len(myName)):  # 'len(myName)' returns the length of the string, used to iterate over each index
    # Print the ASCII (Unicode) value of the character at index 'x'
    print(ord(myName[x]))  # 'ord()' function returns the Unicode code point of the character
