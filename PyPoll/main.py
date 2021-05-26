#Import the os module to create a file paths across operating systems
import os

#Import the module to read the CSV files
import csv


#Set the path to the csv file
csvpath = os.path.join('resources', 'election_data.csv')

#Set the needed variables

total_votes_counter = 0
election_candidate_list = []
candidate_dict = {}

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

            #Create list containing candidates
            if row[2] not in election_candidate_list:
                election_candidate_list.append(row[2])

#Create a dictionary using the candidates from the elaction_candidate_list to store the votes in
for key in election_candidate_list:
    candidate_dict[key] = 0

#Read the csv file again
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)
    
    #Loop through csv file and store each vote to the dictionary
    for row in csvreader:
        candidate_dict[row[2]] += 1

#Find the Winner
winner = max(candidate_dict, key=candidate_dict.get)

#Print results to the terminal

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes_counter)}")
print("--------------------------")
for key in candidate_dict:
    print(key + ": " + str(round((candidate_dict[key] / total_votes_counter)*100, 3))+"% ("+str(candidate_dict[key])+")")
print("--------------------------")
print(f"Winner: {winner}")

#Create an output file path
output_path = os.path.join('analysis','pypoll_analysis.txt')

#Open the file using the "write mode"
with open(output_path, 'w') as file:

    #Write Results in the text file
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {str(total_votes_counter)}\n")
    file.write("--------------------------\n")
    for key in candidate_dict:
            file.write(key + ": " + str(round((candidate_dict[key] / total_votes_counter)*100, 3))+"% ("+str(candidate_dict[key])+")\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {winner}\n")