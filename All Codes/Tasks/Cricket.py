# Initialize an empty list to store runs for each over
oversList = []
# Initialize a variable to keep track of the total runs scored
overTotal = 0

# Loop to get runs for 5 overs
for x in range(5):
    # Append an empty list for each over to store runs for that over
    oversList.append([])

    # Loop to get runs for 6 balls in the current over
    for y in range(6):
        # Prompt the user to enter runs scored for the current ball
        overRuns = int(input("Over " + str(x + 1) + " ball " + str(y + 1) + " how many runs did you get?: "))
        
        # Validate the input to ensure runs are between 0 and 6 (inclusive)
        while overRuns > 6 or overRuns < 0:
            # If input is invalid, prompt the user to re-enter runs
            overRuns = int(input("Please re-enter: "))
        else:
            # Append the valid runs to the respective over in the oversList
            oversList[x].append(overRuns)
            # Add the runs to the total score
            overTotal = overTotal + overRuns

# Initialize a counter for overs
count = 1
# Loop through each over in the oversList to print the runs for each over
for overs in oversList:
    print("Overs", count, "is", overs)  # Print the runs for the current over
    count += 1  # Increment the over count

# Print the total score at the end
print("The final score was", overTotal, "runs.")

# The following code is commented out as it appears to be unrelated to the main function of the code

##fruitList=["cherry","papaya","rose apple", "passion fruit"]
#print(fruitList)

##for henna in fruitList:
##    print(henna)

##for atriedes in range(0,4):
##    print(fruitList[atriedes])
