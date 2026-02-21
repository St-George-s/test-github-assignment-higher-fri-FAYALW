#Pseudocode:
#outputduplicates(tempReadings, readingDates, middle, target)

#Python:
def outputDuplicates(tempReadings, readingDates, middle, target):
    left = middle
    right = middle
    while left>0 and tempReadings[left-1] == target:
        left = left - 1
    while right<len(tempReadings) - 1 and tempReadings[right+1] == target:
        right = right + 1
    for i in range(left, right+1):
        print(readingDates[i], " ", tempReadings[i])

tempReadings = [3.1,3.1,3.1,3.2,3.2]
readingDates = ["21Jan25", "11Feb25", "29Jan25", "01Feb25", "03Mar25"]

outputDuplicates(tempReadings, readingDates, 2, 3.1)
