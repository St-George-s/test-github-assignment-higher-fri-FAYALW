# Function to perform linear search on parallel arrays
def linear_search_parallel_arrays(names, scores, target_name):
    """
    Performs a linear search on two parallel arrays (names and scores).
    
    Parameters:
    names (list): Array of names (strings) corresponding to individuals.
    scores (list): Array of scores (integers) corresponding to each name.
    target_name (str): The name we are searching for.

    Returns:
    int: The score of the target name if found, else None.
    """

    # Loop through the 'names' array to find the target_name
    for i in range(len(names)):
        # Check if the current name matches the target name
        if names[i] == target_name:
            # Return the corresponding score from the scores array
            return scores[i]
    
    # Return None if the target name was not found
    return None

# Example parallel arrays
names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [88, 92, 75, 85]

# Example usage
target_name = "Charlie"
result = linear_search_parallel_arrays(names, scores, target_name)

# Print the result
if result is not None:
    print(f"The score for {target_name} is {result}.")
else:
    print(f"{target_name} not found.")
