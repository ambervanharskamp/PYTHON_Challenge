#Import the os module to create a file paths across operating systems
import os

#Import the module to read the CSV files
import csv

#Set the path to the csv file
csvpath = os.path.join('resources', 'election_data.csv')

#Set the needed variables

total_votes_counter = 0

#Read the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)

    #Go to the first row of the data
    first_data_row = next(csvreader)

    #Count the first month in the first row of the data 
    total_votes_counter = 1

    #Start the loop through the csv rows
    for row in csvreader:

            #Add each row to the total_months_counter
            total_votes_counter +=1

#Format results to print to the terminal
message = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {str(total_votes_counter)}\n"\
    f"--------------------------\n"
 
    f"--------------------------\n" 
)

#Print message to the terminal
print(message)

#Create an output file path
output_path = os.path.join('analysis','pypoll_analysis.txt')

#Open the file using the "write mode"
with open(output_path, 'w') as file:

    #Write Results in the text file
    file.write(message)