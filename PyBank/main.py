import csv
import os
import pandas as pd 
import sys

csvpath = os.path.join("Resources", "Data.csv")

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
total_months = 0
net = 0
month_count = []
profit = []
change_profit = []

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if any(month in cell for cell in row for month in months):
            total_months = total_months + 1

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for file in reader:  
        df = pd.read_csv(csvpath)  
        net = df['Profit/Losses'].sum()

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    for row in reader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

increase = max(change_profit)
decrease = min(change_profit)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1   






        
            

print("Financial Analysis")
print("--------------------------------------")     
print("Total Months: " + (str(total_months)))  
print("Total: " + (str(net)))
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      


filename = open(os.path.join("analysis", "Financial Analysis.txt"),'w')
sys.stdout = filename
print("Financial Analysis")
print("--------------------------------------")     
print("Total Months: " + (str(total_months)))  
print("Total: " + (str(net)))
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")   
sys.stdout.close()
