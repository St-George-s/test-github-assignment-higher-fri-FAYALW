# Arrays to store first names, last names, and heights
firstNames = ['John', 'Sarah', 'Mark', 'Hazel']  # List of first names
lastNames = ['Smith', 'Brown', 'Green', 'Snape']  # List of last names
heights = [169, 158, 140, 172]  # List of corresponding heights in centimeters

# Loop through the range of the length of the firstNames list
for count in range(len(firstNames)):  # Iterate over each index in the firstNames list
    print(firstNames[count])  # Print the first name at the current index
    print(lastNames[count])  # Print the last name at the current index
    print(heights[count])  # Print the height at the current index
