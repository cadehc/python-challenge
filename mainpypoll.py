import os
import csv

csvpath = os.path.join('python-challenge-main', 'PyPoll', 'Resources', 'election_data.csv')

#Total Votes
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvfile)
    print(f'Header: {csvheader}')

    votes = 0
    for row in csvreader:
        votes = votes + 1
    print(votes)

#Candidates
candidate_list = ['Khan', 'Correy', 'Li', "O'Tooley"]
print(candidate_list)

#Vote Percentage
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvfile)
    print(f'Header: {csvheader}')

K_total = 0
C_total = 0
L_total = 0
O_total = 0
for row in csvreader:
    K_total += int(row[])
