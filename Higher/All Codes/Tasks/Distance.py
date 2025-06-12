# Prompt the user to enter the distance between point A and point B in miles
AB = float(input("Please enter the distance between point A and point B in miles: "))

# Convert the distance from miles to kilometers (1 mile = 1.6 kilometers)
KM = AB * 1.6

# Calculate the circumference of a circle using the formula C = π * d
# Here, we assume the distance represents the diameter of the circle
PI = KM * 3.142

# Calculate half of the circumference
Half = PI / 2

# Print the calculated half circumference
print("The distance is: ", Half)
