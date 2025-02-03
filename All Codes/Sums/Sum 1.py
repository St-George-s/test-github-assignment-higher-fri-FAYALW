# Speed camera program to calculate average speed

# Prompt the user to enter the time taken (in minutes) for a car to drive 2km
time = int(input("enter an amount of time for a car to drive 2km in minutes "))  # Convert user input to an integer

# Prompt the user to enter a distance (in kilometres) 
distance = int(input("please enter a distance in kilometres "))  # Convert user input to an integer

# Calculate the average speed:
# 1. Convert distance from kilometres to meters (1 km = 1000 meters)
# 2. Convert time from minutes to seconds (1 minute = 60 seconds)
# Average speed formula: speed = distance / time
ave_speed = (distance * 1000) / (time * 60)  # Calculate average speed in meters per second

# Print the calculated average speed
print(ave_speed)  # Output the average speed
