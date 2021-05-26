#Import the os module to create file paths across operating systems
import os

#Import the module to read the CSV files
import csv

#Set the path to the csv file
csvpath = os.path.join('resources','budgetdata.csv')

#Set the needed variables

total_months_counter = 0
net_profitloss_total = 0
profitloss_previous_month = 0
profitloss_current_month = 0
monthly_change=0
monthly_change_list = []
date_list = []

#Create a function to find the average from the monthly_change_list
def Average(monthly_change_list):
    return sum(monthly_change_list) / len(monthly_change_list)

#Read the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)

    #Go to the first row of the data
    first_data_row = next(csvreader)

    #Count the first month in the first row of the data 
    total_months_counter = 1

    #Add the first profit/loss to the net_profitloss_total
    net_profitloss_total += int(first_data_row[1])

    #Give profitloss_previous_month the profit/loss value for the first month
    profitloss_previous_month = int(first_data_row[1]) 

    #Start the loop through the csv rows
    for row in csvreader:

            #Add each row to the total_months_counter
            total_months_counter +=1

            #Add the date to the date_list
            date_list.append(str(row[0]))

            #Add each profit / loss to the net_profitloss_total
            net_profitloss_total = net_profitloss_total + int(row[1])

            #Give profitloss_current_month the profit/loss value for the first month
            profitloss_current_month = int(row[1])

            #Calculate the monthly_change
            monthly_change = profitloss_current_month - profitloss_previous_month

            #Add the monthly_change to the monthly_change_list
            monthly_change_list.append(monthly_change)

            #Reset the value of profitloss_previous_month to that of profitloss_current_month 
            profitloss_previous_month = profitloss_current_month

#Calculate the average of the values in the monthly_change_list
average = Average(monthly_change_list)

#Find the greatest increase in profit
greatest_increase_profit = max(monthly_change_list)

#Find the greatest decrease in profit
greatest_decrease_profit = min(monthly_change_list)

#Find the index for the greatest increase in profit
greatest_increase_index = monthly_change_list.index(greatest_increase_profit)

#Find the index for the greatest decrease in profit
greatest_decrease_index = monthly_change_list.index(greatest_decrease_profit)

#Find the date for the greatest increase in profit
greatest_increase_date = date_list[greatest_increase_index]

#Find the date for the greatest decrease in profit
greatest_decrease_date = date_list[greatest_decrease_index]

#Format results to print to the terminal
message = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {str(total_months_counter)}\n"\
    f"Total: ${str(net_profitloss_total)}\n"
    f"Average Change: ${str(round(average,2))}\n"\
    f"Greatest Increase in Profits: {date_list[greatest_increase_index]} (${str(greatest_increase_profit)})\n"
    f"Greatest Decrease in Profits: {date_list[greatest_decrease_index]} (${str(greatest_decrease_profit)})\n"
    f"--------------------------\n" 
)

#Print message to the terminal
print(message)

#Create an output file path
output_path = os.path.join('analysis','pybank_analysis.txt')

#Open the file using the "write mode"
with open(output_path, 'w') as file:

    #Write Results in the text file
    file.write(message)