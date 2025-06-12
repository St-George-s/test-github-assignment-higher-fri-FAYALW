# Bubble sort
import random  # Import the random module to generate random numbers (not used in this snippet)

# Bubble Sort Function
def bubble_sort(list):  # Define a function that takes a list as input
    total_swaps = 0  # Initialize a counter for the total number of swaps
    list_to_sort_length = len(list)  # Get the length of the list to be sorted
    swapped = True  # Initialize a variable to track if a swap occurred

    print("BUBBLE START: Sorting the list", list)  # Print the starting list for debugging

    # The outer while loop will repeat if there has been a swap and there is more than one item in the list
    # Each iteration will bubble the largest number to the end of the list
    while swapped and list_to_sort_length >= 0:
        print("\tWHILE START: Swapped is " + str(swapped) + " and list_to_sort_length is " + str(list_to_sort_length) + " so repeating while loop")
        swapped = False  # Reset swapped for this iteration

        # The inner for loop goes through the list to compare and swap elements
        for i in range(0, list_to_sort_length - 1):
            print("\t\tFOR Iteration " + str(i))
            print("\t\t\tComparing index " + str(i) + " with " + str(i + 1))

            # If the value in position i is greater than the one in position i+1, swap them
            if list[i] > list[i + 1]:
                print("\t\t\t" + str(list[i]) + " is greater than " + str(list[i + 1]) + " so swapping")
                print("\t\t\t" + str(list))

                # Swap the elements
                temp = list[i]  # Store the current element in a temporary variable
                list[i] = list[i + 1]  # Move the next element to the current position
                list[i + 1] = temp  # Place the current element in the next position
                total_swaps += 1  # Increment the total swaps counter

                # Prepare output for visualization
                unswapped_lower = str(list[0:i] if len(list[0:i]) > 0 else "") + " "
                swapped = "\033[1m" + str(list[i + 1]) + " <-> " + str(list[i]) + ", " + "\033[0m"
                unswapped_higher = str(list[i + 2:] if len(list[i + 2:]) > 0 else "") + " "

                # Print the current state of the list after the swap
                print("\t\t\t" + unswapped_lower + swapped + unswapped_higher)
                print("\t\t\t" + str(list))
                swapped = True  # A swap has occurred, so set swapped to True
            else:
                print("\t\t\tNo Swap")  # No swap was made, print the status

        # The value at the end of the current pass is now in its correct position
        list_to_sort_length -= 1  # Reduce the length of the unsorted portion
        print("\tWHILE END: Swapped is " + str(swapped) + ", list_to_sort_length is " + str(list_to_sort_length) + ", and list is", list)

    print("BUBBLE END: Sorted list is ", list)  # Print the sorted list
    print("Total swaps is ", total_swaps)  # Print the total number of swaps made


# Main program execution
if __name__ == '__main__':
    # Call bubble_sort with a sample list to demonstrate functionality
    # bubble_sort([5, 1, 4, 8, 2, 9])
    # bubble_sort([5, 1, 4, 8, 2, 12, 9])
    # bubble_sort([8, 8, 8, 4, 8, 3])
    bubble_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # bubble_sort([random.randint(1, 10) for x in range(0, 50)])  # Generates a list of 50 random integers from 1 to 10 and sorts it
