import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

def calculate_column_averages(columns):
    """
    Calculates the average of each column containing numeric values.

    Args:
        columns (list): A list of lists where each inner list represents a column.

    Returns:
        list: A list of averages for numeric columns. Non-numeric columns are skipped.
    """
    averages = []
    for column in columns:
        # Filter out non-numeric values
        numeric_values = [value for value in column if isinstance(value, int)]
        if numeric_values:  # Only calculate average if there are numeric values
            averages.append(statistics.mean(numeric_values))
        else:
            averages.append(None)  # Indicate non-numeric columns with None
    return averages

def calculate_column_medians(columns):
    """
    Calculates the median of each column containing numeric values.

    Args:
        columns (list): A list of lists where each inner list represents a column.

    Returns:
        list: A list of medians for numeric columns. Non-numeric columns are skipped.
    """
    medians = []
    for column in columns:
        # Filter out non-numeric values
        numeric_values = [value for value in column if isinstance(value, int)]
        if numeric_values:  # Only calculate median if there are numeric values
            medians.append(statistics.median(numeric_values))
        else:
            medians.append(None)  # Indicate non-numeric columns with None
    return medians


if __name__ == "__main__":
    file_path = 'icecreamsales.csv'  # Replace with your CSV file path
    rows, columns = csv_to_lists(file_path)
    print("Rows:", rows)
    print("Columns:", columns)

    averages = calculate_column_averages(columns)
    print("Column Averages:", averages)
    print(f"Average Temperature = {averages[0]} degrees")
    print(f"Average Sales =  €{averages[1]}")

    medians = calculate_column_medians(columns)
    print("Column Medians:", medians)
    print(f"Median Temperature = {medians[0]} degrees")
    print(f"Median Sales =  €{medians[1]}")
    

# Read in ice cream sales data
ics_df = pd.read_csv('icecreamsales.csv')
#this csv only has 2 columns
ics_df = ics_df.sort_values(by='Temperature')

# Convert from Pandas to NumPy array
np_arr = ics_df.values

# Get x & y values and put in array
x_2 = np_arr[:,0]
y_2 = np_arr[:,1]

fig_4 = plt.figure(figsize=(6,4))
axes_4 = fig_4.add_axes([0,0,1,1])
axes_4.set_title('Ice Cream Sales vs. Temperature')
axes_4.set_xlabel('Temperature')
axes_4.set_ylabel('Ice Cream Sales')
axes_4.plot(x_2,y_2)

# Add Annotations by supplying the x & y to point at and the position of the text
# based off of lower left had corner being 0,0
axes_4.annotate('Good Month', xy=(83, 536), xytext=(60, 520),
             arrowprops=dict(facecolor='black', shrink=0.05),)

# Add bars to the plot
plt.bar(x_2,y_2)
plt.show()

