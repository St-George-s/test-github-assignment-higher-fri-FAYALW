def linear_search(numbers, item_to_find):
    found = False
    counter = 0
    array_size = len(numbers)
    while counter < array_size and not found:
        if numbers[counter] == item_to_find:
            found = True
        else:
            counter += 1
    if found:
        print(f"{item_to_find} found at position {counter}")
    else:
        print("Item not found")
# Example usage:
numbers = [5, 3, 7, 1, 4]
linear_search(numbers, 7)