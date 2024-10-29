# timesSpent = [5,3,4,6,5]
# def findMax(timeSpent): 
#     maximumValue = timeSpent[0] 
#     for counter in range(1, len(timeSpent)): 
#         if timeSpent[counter] > maximumValue: 
#             maximumValue = timeSpent[counter] 
#     print(f"The largest value was {maximumValue}") 
# findMax(timesSpent)

#timesSpent = [5,3,4,6,5]
# def findMin(timesSpent): 
#     minimumValue = timesSpent[0] 
#     for count in range(len(timesSpent)): 
#         if timesSpent[count] < minimumValue: 
#             minimumValue = timesSpent[count] 
#     print(f"The smallest value was {minimumValue}") 
# findMin(timesSpent)


def linearSearch(timesSpent, itemToFind): 
    found = False 
    counter = 0 
    arraySize = len(timesSpent) 
    while counter < arraySize and not found: 
        if timesSpent[counter] == itemToFind: 
            found = True 
        else: 
            counter += 1 
    if found: 
        print(f"{itemToFind} found at position {counter}") 
    else: 
        print("Item not found") 

timesSpent = [5,3,4,6,5]
itemToFind = int(input("Enter the number you would like to find: "))

linearSearch(timesSpent, itemToFind)
