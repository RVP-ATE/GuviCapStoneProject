import openpyxl
import os


def get_login_data(filename):
    # Dynamically get the full path to the Excel file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get path to current script directory
    file_path = os.path.join(base_dir, '..', 'TestData', filename)  # Build path to the Excel file
    file_path = os.path.normpath(file_path)  # Normalize the path for OS compatibility

    # Check if the file exists before proceeding
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {filename} was not found at {file_path}")

    # Load the workbook and access the sheet
    wb = openpyxl.load_workbook(file_path)  # Open the workbook
    sheet = wb.active  # Access the active sheet, or specify a sheet name like wb['Sheet1']

    data = []  # Initialize an empty list to store the login data (username, password)

    # Iterate over each row starting from the second row (skip header)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username = row[5]  # Get the username from the 6th column (index 5)
        password = row[6]  # Get the password from the 7th column (index 6)

        # Check if both username and password are present, else skip the row
        if username and password:
            data.append((username, password))  # Add the username-password tuple to the list
        else:
            print(f"Skipping invalid row: {row}")  # Print a message if the row is invalid

    wb.close()  # Close the workbook to release resources
    return data  # Return the list of username-password pairs
