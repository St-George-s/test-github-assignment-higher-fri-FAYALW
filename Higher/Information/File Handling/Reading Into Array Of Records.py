import csv

# Function to read a CSV file into an array of records (list of lists)
def read_csv_to_array(file_name):
    records = []
    
    # Open the CSV file and read it using the csv module
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over the rows in the CSV reader
        for row in csv_reader:
            records.append(row)  # Append each row (record) to the array
    
    return records

# Example usage
file_name = 'data.csv'  # Replace with your file path
records_array = read_csv_to_array(file_name)

# Output the array of records
for record in records_array:
    print(record)