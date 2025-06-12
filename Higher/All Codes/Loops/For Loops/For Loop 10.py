def calculate_average(grades: list) -> float:
    """Calculate the average of a list of grades."""
    numberOfGrades = len(grades)  # Get the total number of grades
    total = sum(grades)  # Calculate the sum of all grades
    return total / numberOfGrades  # Return the average (total divided by the number of grades)

def find_highest_grade(grades: list) -> float:
    """Find and return the highest grade from the list."""
    return max(grades)  # Use the max function to find the highest grade

def find_lowest_grade(grades: list) -> float:
    """Find and return the lowest grade from the list."""
    return min(grades)  # Use the min function to find the lowest grade

def print_student_report(names: list, grades: list) -> None:
    """Prints a report of students and their grades, along with the highest, lowest, and average grades."""
    # Loop through the list of names and grades
    for x in range(len(names)):
        print(names[x] + str(grades[x]))  # Print each student's name and their corresponding grade
    
    # Print the highest, lowest, and average grades by calling the respective functions
    print("The highest grade is", find_highest_grade(grades), 
          "the lowest grade is", find_lowest_grade(grades), 
          "the average grade is", calculate_average(grades))

# List of student names
names = ["Alice ", "Bob ", "Charlie "]  
# List of corresponding grades for each student
grades = [95.5, 87.0, 92.5]  

# Call the function to print the student report
print_student_report(names, grades)

# Uncomment the following line to print just the average grade
#print(calculate_average(grades))  