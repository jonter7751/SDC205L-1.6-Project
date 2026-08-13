from datetime import datetime

print("jonter7751 Spreadsheet Automation Menu")

print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# the next line retrieves the inputted option and stores into the variable called choice.
choice = input("Enter your choice (1-3): ")

print("You have selected", choice, "at", str(datetime.now()))
