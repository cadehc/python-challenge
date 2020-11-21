import os
import csv

#Total months
csvpath = os.path.join('python-challenge-main', 'PyBank', 'Resources', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvfile)
    print(f'Header: {csvheader}')

    months = 0
    for row in csvreader:
        months = months + 1
    print(months)

#Net Total

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvfile)
    print(f'Header: {csvheader}')
    
    net_total = 0
    for row in csvreader:
        net_total += int(row[1])
        net_total = sum(iter(iterable[net_total])
    print(net_total)

# Average change in profits/losses
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvfile)
    print(f'Header: {csvheader}')

    average_profit = 0
    for column in csvreader:
        average_profit = average('B2:B87')
    print(average_profit)

#Biggest Increase
    big_inc = int(row[1])
#Biggest Decrease
    big_dec = int(row[0])