#PyBank python script. Homework 3

import csv
import os


pyBankCSV = os.path.join("Resources", "budget_data.csv")


with open(pyBankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    next(csvreader, None)
    totPnl = 0.00
    totMth = 0 
    totChangeCnt = 0 
    totChange = 0.00
    maxDiff = 0.00
    minDiff = 0.00 
    prevMonth = 0
    DiffCnt = 0
    Diff = 0.00
    DiffDict = {}
    for row in csvreader:
        date = row[0]
        pnl = float(row[1])
        totMth = totMth+1

        totPnl = totPnl + pnl

        #difference between months
        if totMth == 0:
            maxDiff = 0
            prevMonth = pnl
        else:
            Diff = pnl - prevMonth
            
            
            if Diff > maxDiff:
                DiffDict["MaxMonth"] = row[0]
                DiffDict["MaxDiff"] = '${:,.2f}'.format(Diff)
                #update MaxDiff after comparison
                maxDiff = Diff
            if Diff < minDiff:
                DiffDict["MinMonth"] = row[0]
                DiffDict["MinDiff"] = '${:,.2f}'.format(Diff)
                #update MaxDiff after comparison
                minDiff = Diff
            if totMth > 1:

                totChangeCnt = totChangeCnt +1
                totChange = totChange + Diff
            prevMonth = pnl

#Compile satement string (broken out to make reading easier)
FinalStatement =(f"Total Months: {totMth}\nTotal: {'${:,.2f}'.format(totPnl)}\nAverage Change: {'${:,.2f}'.format(totChange/totChangeCnt)}")
FinalStatement = FinalStatement + (f"\nGreatest Change in Profits: {DiffDict['MaxMonth']} {DiffDict['MaxDiff']}")
FinalStatement = FinalStatement + (f"\nGreatest Decrease in Profits: {DiffDict['MinMonth']} {DiffDict['MinDiff']}")

print(FinalStatement)

Output_File = os.path.join("Resources","Output.txt")
with open(Output_File,"w") as txtFile:
    txtFile.write(FinalStatement)
