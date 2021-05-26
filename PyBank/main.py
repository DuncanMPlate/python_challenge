import csv
import os
import math

output_path = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')


#open file in write mode
with open(output_path, 'r', newline='') as csvfile:
    #initialise writer
    csvreader = csv.reader(csvfile, delimiter=',')
    for r in csvreader:
        print(csvfile)


