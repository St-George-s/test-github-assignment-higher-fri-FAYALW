import math  # Importing the math library for floor function

# Function to perform binary search on a sorted list
def binary_search(list, target):
    low = 0  # Initialize the lower bound of the search range
    high = len(list) - 1  # Initialize the upper bound of the search range
    mid = 0  # Variable to hold the midpoint of the search range
    found = False  # Flag to indicate if the target is found
    elements_searched = 0  # Counter to keep track of elements searched

    # Loop continues until target is found or range is exhausted
    while found == False and low <= high:
        mid = (low + high) / 2  # Calculate the midpoint
        mid = math.floor(mid)  # Convert to an integer using floor division

        # Check if the target is at the midpoint
        if target == list[mid]:
            print("found at position " + str(mid))  # Print the position if found
            found = True  # Set the flag to True indicating target is found

        # If target is greater than the midpoint, adjust the lower bound
        elif target > list[mid]:
            low = mid + 1

        # If target is less than the midpoint, adjust the upper bound
        else:
            high = mid - 1

        # If target is not found after checking the current midpoint
        if not found:
            print("Target not found")  # Print message indicating target not found

    print("Searched " + str(elements_searched) + " elements")  # Print the number of elements searched
    return {"found": found, "elements_searched": elements_searched, "position": mid}  # Return search results

# Main execution
if __name__ == '__main__':
    binary_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 27)  # Test binary search with a sample list and target
