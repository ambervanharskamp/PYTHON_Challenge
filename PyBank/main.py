#Import the os module to create a file paths across operating systems
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

print({str(total_months_counter)})
print({str(net_profitloss_total)})
print ({str(monthly_change_list)})
print ({str(date_list)})
print ({str(round(average,2))})
print ({str(greatest_increase_profit)})
print ({str(greatest_decrease_profit)})


