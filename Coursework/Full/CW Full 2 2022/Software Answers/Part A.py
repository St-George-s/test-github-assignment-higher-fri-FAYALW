# 1a)
# That the data was added during the month of September
# That the data is valid

# 1b)
def upperCase(word): #Defines function
    firstChar = ord(word[0]) #Changes the first character of the word to its ASCII value
    if firstChar >=97 and firstChar <= 122: #Checks if the ASCII value is between 97 and 122
        firstChar = firstChar - 32 #Subtracts 32 from the ASCII value
        firstChar = chr(firstChar) #Updates the firstChar variable
        word = (firstChar + word[1:]) #Concatenation
    return word #Returns the new word

# 1c)
# (Part B)

#1d)
#The watchpoint could be put on the line of the variable called count. When count is 6 it should move to the 
# next date. If it does this then it is working, but if it doesn't then it is not

#1e)
#It is efficient as it is only one function that can be reused many times
#Only changes the character if the character is lower case
#Could be more efficient because it doesn't check if the first letter is upper case or not, it converts it to ASCII anyway

#It is maintainable as I have a function for everything meaning they can be reused
#Each function can be edited by itself without affecting the other functions
#As I used functions there are no global variables which reduces errors and mistakes