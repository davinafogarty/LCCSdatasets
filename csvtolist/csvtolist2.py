import csv

def csv_to_lists(file_path):
    """
    Converts a CSV file into a list of lists, casting any numeric values to integers.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of lists representing the rows of the CSV file with numeric values cast to integers.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            processed_row = []
            for value in row:
                if value.isdigit():
                    processed_row.append(int(value))
                else:
                    processed_row.append(value)
            data.append(processed_row)
    return data

# Example usage
if __name__ == "__main__":
    file_path = 'icecreamsales.csv'  # Replace with your CSV file path
    lists = csv_to_lists(file_path)
    print(lists)
