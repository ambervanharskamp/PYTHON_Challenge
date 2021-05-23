#Import the os module to create a file paths across operating systems
import os

#Import the module to read the CSV files
import csv

#Set the path to the csv file
budget_csv = os.path.join('resources', 'budget_data.csv')

#Open and read the csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Skip the header
    csv_header = next(csv_file)
    