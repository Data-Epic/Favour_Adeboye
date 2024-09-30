import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Authenticate and connect to Google Sheets API
def authenticate():
    try:
        # Define the scope of access to Google Sheets and Google Drive
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # Provide the path to your credentials.json file
        creds = ServiceAccountCredentials.from_json_keyfile_name('manifest-alpha-363108-fb069bca3c7c.json', scope)
        
        # Authorize and connect with gspread
        client = gspread.authorize(creds)
        
        # Open the Google Sheet by name
        sheet = client.open("Automation Task").sheet1
        return sheet
    except Exception as e:
        print("Error in authentication: ", e)
        return None

# Read Data from Google Sheet
def read_data(sheet):
    try:
        data = sheet.get_all_records()  # Fetch all records as a list of dictionaries
        print("Data in the sheet:", data)
        return data
    except Exception as e:
        print("Error reading data: ", e)

# Write Data to Google Sheet
def write_data(sheet, row_data):
    try:
        sheet.append_row(row_data)  # Append a new row at the end of the sheet
        print(f"Row {row_data} added to the sheet.")
    except Exception as e:
        print("Error writing data: ", e)

# Update Data in Google Sheet (e.g., updating cell at row 2, column 3)
def update_data(sheet, row, col, new_value):
    try:
        sheet.update_cell(row, col, new_value)
        print(f"Updated cell at row {row}, col {col} with new value: {new_value}")
    except Exception as e:
        print("Error updating data: ", e)

# Delete a Row in Google Sheet
def delete_data(sheet, row):
    try:
        sheet.delete_row(row)  # Delete row by number
        print(f"Row {row} deleted.")
    except Exception as e:
        print("Error deleting data: ", e)

# Automate the script to run periodically (e.g., every 60 seconds)
def automate_task(sheet):
    while True:
        data = read_data(sheet)
        
        # Example task: Calculate sum of values in the second column and write the result
        try:
            values = [int(row['Column2']) for row in data if row['Column2'].isdigit()]
            total_sum = sum(values)
            print(f"Sum of Column2: {total_sum}")
            
            # Write the result back to the sheet in a specific cell (e.g., A10)
            sheet.update_acell('A10', f"Sum of Column2: {total_sum}")
        except Exception as e:
            print("Error in automation task: ", e)
        
        # Run the task every 60 seconds
        time.sleep(60)

if __name__ == "__main__":
    # Authenticate and connect to Google Sheet
    sheet = authenticate()

    if sheet:
        # Read initial data from the sheet
        read_data(sheet)

        # Example: Write a new row of data
        new_row = ["2024-09-17", "New Task", 500]
        write_data(sheet, new_row)

        # Example: Update a cell in row 2, column 3
        update_data(sheet, 2, 3, "Updated Value")

        # Example: Delete a row (e.g., row 3)
        delete_data(sheet, 3)

        # Automate task every 60 seconds
        automate_task(sheet)