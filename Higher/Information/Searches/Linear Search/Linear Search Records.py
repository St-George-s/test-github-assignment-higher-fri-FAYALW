def linear_search(records, target):
    """
    Searches for a target in a list of records using linear search.
    
    Parameters:
        records (list): The list of records to search through.
        target: The target value to search for in the records.
    
    Returns:
        int: The index of the target in records if found, otherwise -1.
    """
    for index, record in enumerate(records):
        if record == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
records = ["Alice", "Bob", "Charlie", "Diana"]
target = "Charlie"

result = linear_search(records, target)
if result != -1:
    print(f"Record '{target}' found at index {result}.")
else:
    print(f"Record '{target}' not found.")