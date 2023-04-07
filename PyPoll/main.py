import csv
import os
import sys
import pandas as pd 

Candidate = "Raymon Anthony Doane"
Candidate1 = "Charles Casper Stockham"
Candidate2 = "Diana DeGette"


csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    lines = len(list(reader))
    lines = lines - 1

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    total_votes_count = -1 
    Charles = 0
    Diana = 0
    Raymon = 0
    Charles_percent = 0
    Diana_percent = 0
    Raymon_percent = 0
    for row in reader:
        total_votes_count += 1
        if row[2] == "Raymon Anthony Doane":
            Raymon = Raymon + 1
        elif row[2] == "Charles Casper Stockham":
            Charles = Charles + 1 
        elif row[2] == "Diana DeGette":
            Diana = Diana + 1 
    Results = {"Raymon Anthony Doane":Raymon, "Charles Casper Stockham":Charles, "Diana DeGette":Diana}
    Charles_percent = round((Charles / total_votes_count) * 100, 3)
    Diana_percent = round((Diana / total_votes_count) * 100, 3)
    Raymon_percent = round((Raymon / total_votes_count) * 100, 3)
    winner = max(Results, key=Results.get)

print("Election Results")
("----------------------------")
print("Total Votes: " + (str(total_votes_count)))
print("----------------------------")
print("Raymon Anthony Doane: " + (str(Raymon_percent) + "%" + " " + (str(Raymon))))
print ("Diana DeGette: " + (str(Diana_percent) + "%" +" " + (str(Diana))))
print ("Charles Casper Stockham: " + (str(Charles_percent) + "%" + " " + (str(Charles))))
print("----------------------------")
print ("Winner: " + (str(winner))) 
print("----------------------------")

filename = open(os.path.join("analysis", "Election Results.txt"),'w')
sys.stdout = filename
print("Election Results")
("----------------------------")
print("Total Votes: " + (str(total_votes_count)))
print("----------------------------")
print("Raymon Anthony Doane: " + (str(Raymon_percent) + "%" + " " + (str(Raymon))))
print ("Diana DeGette: " + (str(Diana_percent) + "%" +" " + (str(Diana))))
print ("Charles Casper Stockham: " + (str(Charles_percent) + "%" + " " + (str(Charles))))
print("----------------------------")
print ("Winner: " + (str(winner))) 
print("----------------------------") 
sys.stdout.close()



