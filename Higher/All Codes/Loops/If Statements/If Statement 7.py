# Finds out if you are speeding (fine, warning, no action)

# Prompt the user to enter the driver's speed in mph and convert the input to an integer
speed = int(input("enter the driver's speed (mph): "))  

# Check if the speed is more than 75 mph
if speed > 75:  # If the speed exceeds 75...
    print("issue fine")  # ...issue a fine for speeding

# Check if the speed is more than 70 mph (but not more than 75)
elif speed > 70:  # Else if the speed exceeds 70 but is 75 or less...
    print("issue driver warning")  # ...issue a warning to the driver

# If the speed is 70 mph or less
else:  # If the speed is 70 or below...
    print("no action required")  # ...no action is needed
