import os
import csv

pypoll = os.path.join("Resources", "election_data.csv")

with open(pypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    totalvotes = 0
    

    totalvotes = sum(1 for row in csvreader) - 1

with open(pypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    Khanvotes = 0
    Correyvotes = 0
    Livotes = 0
    Otoolevotes = 0

    for row in csvreader:
        if row[2] == "Khan":
            Khanvotes = Khanvotes + 1
        elif row[2] == "Correy":
            Correyvotes = Correyvotes + 1
        elif row[2] == "Li":
            Livotes = Livotes + 1
        elif row[2] == "O'Tooley":
            Otoolevotes = Otoolevotes + 1
        else:
            print("null")

Khanperc = round((int(Khanvotes)/int(totalvotes))*100)
Correyperc = round((int(Correyvotes)/int(totalvotes))*100)
Liperc = round((int(Livotes)/int(totalvotes))*100)
Otooleperc = round((int(Otoolevotes)/int(totalvotes))*100)

winnerdict = {
    str(Khanperc): "Khan",
    str(Correyperc): "Correy",
    str(Liperc): "Li",
    str(Otooleperc): "Otoole",
}

print("Election results")
print("----------------")
print("Total Votes: " + str(totalvotes))
print("----------------")
print("Khan: " + str(Khanperc) + "%" + " (" + str(Khanvotes) + ")")
print("Correy: " + str(Correyperc) + "%" + " (" + str(Correyvotes) + ")")
print("Li: " + str(Liperc) + "%" + " (" + str(Livotes) + ")")
print("O'Toole: " + str(Otooleperc) + "%" + " (" + str(Otoolevotes) + ")")
print("----------------")
print("Winner: " + winnerdict[str(max(Khanperc, Correyperc, Liperc, Otooleperc))])
print("----------------")