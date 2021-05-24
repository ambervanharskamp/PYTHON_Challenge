#Import the os module to create a file paths across operating systems
import os

#Import the module to read the CSV files
import csv

#Set the path to the csv file
csvpath = os.path.join('resources','budgetdata.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #for row in csvreader:
        #print(row)
    for row in csvreader:
        print(len(profit/losses))