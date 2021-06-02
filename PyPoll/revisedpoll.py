import csv
import os
import math

file_path = os.path.join(os.getcwd(), 'python_challenge', 'PyPoll', 'Resources', 'election_data.csv')
output_file = os.path.join(os.getcwd(), 'python_challenge', 'PyPoll', 'analysis', 'election_solutions.csv')
canidate_votes = {}
canidate = []
with open(file_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    total_votes = 0
    
    headerline = csvfile.readline()
    for row in csvreader:
        total_votes += 1
        canidate = row[2]        
        if canidate in canidate_votes.keys():
            canidate_votes[canidate] += 1
        else:
            canidate_votes[canidate] = 1

print(canidate_votes)
print(canidate)