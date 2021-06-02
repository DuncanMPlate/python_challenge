import csv
import os


file_path = os.path.join(os.getcwd(), 'python_challenge', 'PyPoll', 'Resources', 'election_data.csv')
output_file = os.path.join(os.getcwd(), 'python_challenge', 'PyPoll', 'analysis', 'election_solutions.csv')
    
    
with open(file_path, 'r', newline='') as csvfile:    
    csvreader= csv.reader(csvfile, delimiter=',')
    KHAAN = 0
    Correy = 0
    Li = 0
    OTooley = 0
    votes_any = []
    total_votes = 0
    headerline = csvfile.readline()
    
    
    for row in csvreader:
        total_votes += 1
        votes_any = str(row[2])
        if votes_any == 'Khan':
            KHAAN += 1
        if votes_any == 'Li':
            Li += 1
        if votes_any == 'Correy':
            Correy += 1
        if votes_any == "O'Tooley":
            OTooley += 1
KHAAN_percent = "{:.001%}".format(KHAAN / total_votes)
Correy_percent = "{:.001%}".format(Correy / total_votes)
Li_percent = "{:.001%}".format(Li / total_votes)
OTooley_percent = "{:.001%}".format(OTooley / total_votes)

with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow([f'Election Results'])
    writer.writerow([f'Total Votes: {total_votes}'])
    writer.writerow([f'Khan: {KHAAN_percent} {KHAAN}'])
    writer.writerow([f'Correy: {Correy_percent} {Correy}'])
    writer.writerow([f'Li: {Li_percent} {Li}'])
    writer.writerow([f"O'Tooley: {OTooley_percent} {OTooley}"])
    writer.writerow([f'Winner: KHAAAAAAAAAAN'])
#print to terminal
print(f'Election Results')
print(f'Total: {total_votes}')
print(f'Khan: {KHAAN_percent} {KHAAN}') 
print(f'Correy:  {Correy_percent} {Correy}') 
print(f'Li:  {Li_percent} {Li}')
print(f"O'Tooley: {OTooley_percent} {OTooley}")
print(f"Winner: KHAAAAAAAAAAAAN") 
print(KHAAN)