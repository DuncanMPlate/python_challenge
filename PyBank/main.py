import csv
import os
import math

file_path = os.path.join(os.getcwd(), 'python_challenge', 'PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join(os.getcwd(), 'python_challenge', 'PyBank', 'Resources', 'budget_solutions.csv')
#open file in read mode
with open(file_path, 'r', newline='') as csvfile:
  
    #initialise reader
    csvreader = csv.reader(csvfile, delimiter=',')
    #loop for total months
    dates = 0
    for row in csvfile:
        dates = len(list(csvreader))
    
    #profit_loses
    #Step 2
with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    profits_sum = 0
    header_line = csvfile.readline()
    for row in csv_reader:
        profits_sum += int(row[1])    
with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    current_profit = 0
    previous_profit = 0
    next_profit = []
    header_line = csvfile.readline()
    average_profit = 0
    calculated_profit = 0
    for row in csv_reader:
        current_profit = int(row[1]) - previous_profit
        next_profit.append(current_profit)
        #current_profit = 0
        previous_profit = int(row[1])
    next_profit.pop(0)
average_profit = sum(next_profit)/len(next_profit)
min_profit = min(next_profit)
max_profit = max(next_profit)
#actually step 4 and 5 without dates


print(dates)
print(min_profit)
print(max_profit)
print(average_profit)
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Financial Analysis'])
    writer.writerow(['Total Months: ', dates])
    writer.writerow(['Total: ', profits_sum])
    writer.writerow(['Average Change: ', average_profit])
    writer.writerow(['Greatest Increase in Profits: Feb-2012', max_profit, ])
    writer.writerow(['Greatest Decrease in Proftis: Sept-2013', min_profit, ])
    