import csv
import os
import math

file_path = os.path.join(os.getcwd(), 'python_challenge', 'PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join(os.getcwd(), 'python_challenge', 'PyBank', 'analysis', 'budget_solutions.csv')
#open file in read mode
#with open(file_path, 'r', newline='') as csvfile:
  
    #initialise reader
    #csvreader = csv.reader(csvfile, delimiter=',')
    #loop for total months
   # dates = 0
  #  for row in csvfile:
 #       dates = len(list(csvreader))
    
    #profit_loses
    #Step 2
#with open(file_path, 'r') as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=",")
    #profits_sum = 0
    #header_line = csvfile.readline()
    #for row in csv_reader:
    #    profits_sum += int(row[1])    
with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    current_profit = 0
    previous_profit = 0
    next_profit = []
    dates = 0
    profits_sum = 0
    header_line = next(csv_reader)
    jan_data = next(csv_reader)
    dates = dates +1
    profits_sum = profits_sum + int(jan_data[1])

    average_profit = 0
    calculated_profit = 0
    months = []
    #jandata = next(csv_reader)
    for row in csv_reader:
        dates = dates +1
        profits_sum = profits_sum + int(row[1])
        current_profit = int(row[1]) - previous_profit
        next_profit.append(current_profit)
        #current_profit = 0
        previous_profit = int(row[1])
        months.append(row[0])
       
    next_profit.pop(0)
average_profit = sum(next_profit)/len(next_profit)
min_profit = min(next_profit)
max_profit = max(next_profit)
min_date = next_profit.index(min_profit)
max_date = next_profit.index(max_profit)
#actually step 4 and 5 without dates

print(dates)
print(min_profit)
print(max_profit )
print(round(average_profit,2))
print(months[min_date+1])
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Financial Analysis'])
    writer.writerow([f'Total Months: {dates}'])
    writer.writerow([f'Total: {round(profits_sum,2)}'])
    writer.writerow([f'Average Change: {round(average_profit,2)}'])
    writer.writerow([f'Greatest Increase in Profits: {months[max_date+1]} {max_profit}'])
    writer.writerow([f'Greatest Decrease in Proftis: {months[min_date+1]} {min_profit}'])
    #datafile.write.(output)