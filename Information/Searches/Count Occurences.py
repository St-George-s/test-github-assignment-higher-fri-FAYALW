def count_occurrences(items, item_to_find):
    number_found = 0
    for item in items:
        if item == item_to_find:
            number_found += 1
    print(f"There were {number_found} occurrences of {item_to_find} in the list")

# Example usage:
most_watched = ["comedy", "dance", "music", "dance", "travel", "food", "comedy"]
count_occurrences(most_watched, "dance")