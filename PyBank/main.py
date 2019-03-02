import os
import csv

pybankcsv = os.path.join("Resources","budget_data.csv") 
profitlist = []

with open(pybankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print("Financial Analysis")
    print("------------------")  
    rowcount = sum(1 for row in csvreader) - 1
    print("Total Months: " + str(rowcount))

with open(pybankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    ptotal = 0
    next(csvreader)
    for row in csvreader:
        ptotal += int(row[1])
    print("Total: " + str(ptotal))

pybankcsv = os.path.join("Resources","budget_data.csv") 
with open(pybankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:

        profitlist.append(row[1])   
changelist = []
for x in range(0, rowcount-1):
    changelist.append(int(profitlist[x+1]) - int(profitlist[x]))
    
    
avgchange = sum(changelist)/len(changelist)
print("Average Change: " + str(avgchange))
biggestgain = max(changelist)
biggestloss = min(changelist)

biggestgaindatenumber = changelist.index(biggestgain)
biggestlossdatenumber = changelist.index(biggestloss)

with open(pybankcsv, newline='') as csvfile:
    data = list(csv.reader(csvfile))
    biggestlossdate = data[biggestlossdatenumber+2][0]
    biggestgaindate = data[biggestgaindatenumber+2][0]

print("Greatest increase in Profits: " + biggestgaindate + " (" + str(biggestgain) + ")")
print("Greatest decrease in Profits: " + biggestlossdate + " (" + str(biggestloss) + ")")
