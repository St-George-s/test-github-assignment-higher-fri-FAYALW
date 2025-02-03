def find_min(numbers):
    minimum_value = numbers[0]
    for count in range(len(numbers)):
        if numbers[count] < minimum_value:
            minimum_value = numbers[count]
    print(f"The smallest value was {minimum_value}")
# Example usage:
views = [1000, 20, 150, 500, 6000]
find_min(views)