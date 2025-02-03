def find_max(numbers):
    maximum_value = numbers[0]
    for counter in range(1, len(numbers)):
        if numbers[counter] > maximum_value:
            maximum_value = numbers[counter]
    print(f"The largest value was {maximum_value}")

# Example usage:
views = [1000, 20, 150, 500, 6000]
find_max(views)