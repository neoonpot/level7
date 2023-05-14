import python_readcsv
import python_readcsv2
import python_readcsv3
import csv
import openpyxl
import pandas
# call function from python_readcsv.py
python_readcsv.function_name()

# define function to convert csv to excel
def csv_to_excel(csv_path, excel_path):
    # open the csv file for reading
    with open(csv_path, 'r') as csvfile:
        # create a csv reader object
        csvreader = csv.reader(csvfile)

        # create a new worksheet
        wb = openpyxl.Workbook()
        ws = wb.active

        # loop through each row
        for row in csvreader:
            # write to the row
            ws.append(row)

        # save the excel file
        wb.save(excel_path)

# call the function with the file paths
csv_to_excel('/Users/emanuelsorensen/Semester_projekt/Pythonlevel7/myenv/ITA-1 - System 1.csv', 'ITA-1 - System 1.xlsx')

# call function from python_readcsv2.py
python_readcsv2.function_name()

# call function from python_readcsv3.py
python_readcsv3.function_name()
