# Bubble sort simple
import random  # Import the random module to generate random numbers (not used in this snippet)

# Bubble Sort Function
def bubble_sort(list):  # Define a function that takes a list as input
    n = len(list)  # Get the length of the list
    swapped = True  # Initialize a variable to track if a swap occurred

    # While there are swaps and n is non-negative
    while swapped and n >= 0:
        swapped = False  # Set swapped to False for the current iteration
        # Loop through the list up to the n-1 index
        for i in range(0, n - 1):
            # If the current element is greater than the next element
            if list[i] > list[i + 1]:
                # Swap the elements
                temp = list[i]  # Temporarily store the current element
                list[i] = list[i + 1]  # Move the next element to the current position
                list[i + 1] = temp  # Place the current element in the next position

                swapped = True  # Set swapped to True indicating a swap occurred
        n = n - 1  # Decrease n since the last element is now in its correct position

    print(list)  # Print the sorted list


# Main program execution
if __name__ == '__main__':
    # Call bubble_sort with a sample list to demonstrate functionality
    bubble_sort([5, 1, 4, 8, 2, 9])
    # Additional examples that are commented out for testing purposes
    # bubble_sort([5, 1, 4, 8, 2, 12, 9])
    # bubble_sort([8, 8, 8, 4, 8, 3])
    # bubble_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # bubble_sort([random.randint(1, 10) for x in range(0, 50)])  # Generates a list of 50 random integers from 1 to 10 and sorts it
