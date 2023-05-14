import csv
import openpyxl

#open the csv file for reading
with open('/Users/emanuelsorensen/Semester_projekt/Pythonlevel7/myenv/ITA-3 - System 3.csv', 'r') as csvfile:
    #create a cvs reader objetk
    csvreader = csv.reader(csvfile)

    #create a new worksheet
    wb = openpyxl.Workbook()
    ws = wb.active


    #loop gennem hver fil
    for row in csvreader:
        #skriv til rækken
        ws.append(row)

        # gem til excel filen 
        wb.save('ITA-3 - System 3.xlsx')
