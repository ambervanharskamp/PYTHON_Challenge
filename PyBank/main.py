#Import the os module to create a file paths across operating systems
import os

#Import the module to read the CSV files
import csv

#Set the path to the csv file
csvpath = os.path.join('resources','budgetdata.csv')

#Set the needed variables

total_months_counter = 0

#Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)

    #Go to the first row of the data
    first_data_row = next(csvreader)

    #Count the first month in the first row of the data 
    total_months_counter = 1

    #Start the loop through the csv rows
    for row in csvreader:

            total_months_counter +=1

print({str(total_months_counter)})
