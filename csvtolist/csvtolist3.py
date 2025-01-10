import csv

def csv_to_lists(file_path):
    """
    Converts a CSV file into a list of lists, casting any numeric values to integers, and creates separate lists for each column.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing the list of lists representing rows and a list of lists representing columns.
    """
    rows = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:  # Iterate through each row in the CSV file
            processed_row = []  # Initialize a list to store processed values of the current row
            for value in row:  # Iterate through each value in the current row
                if value.isdigit():  # Check if the value is numeric
                    processed_row.append(int(value))  # Convert the numeric value to an integer and add it to the list
                else:
                    processed_row.append(value)  # Add non-numeric values as-is to the list
            rows.append(processed_row)  # Add the processed row to the rows list

    # Transpose rows to columns
    if rows:  # Check if the rows list is not empty
        columns = [list(column) for column in zip(*rows)]  # Transpose rows to columns using zip and create lists for each column
    else:
        columns = []  # If rows are empty, set columns as an empty list

    return rows, columns

# Example usage
if __name__ == "__main__":
    file_path = 'icecreamsales.csv'  # Replace with your CSV file path
    rows, columns = csv_to_lists(file_path)
    print("Rows:", rows)
    print("Columns:", columns)
