## PyPoll

import os
import csv

pyPollCSV = os.path.join("Resources","election_data.csv")

with open(pyPollCSV,"r") as csvFile:
    csvreader = csv.reader(csvFile, delimiter = ",")

    next(csvreader, None)

    #candidateDic = {'Candidate': None, 'Total Votes':None, 'Percentage':None}
    candidateDic={}
    candidatePercent={}
    totalCount = 0 
    #print(candidateDic)
    for row in csvreader:
        candidateName = row[2]
        totalCount = totalCount +1
        #print(candidateName)
        #candidateCount = candidateCount + 1
        if candidateName  in candidateDic.keys():
            candidateDic[candidateName] =  candidateDic[candidateName]+1
        else:
            candidateDic[candidateName]= 1
            #candidateDic[candidateName] = int(candidateDic[candidateName])+1
            #print('Update dic')

    #update Candidate values once total is found
    for candidate in candidateDic:
        candidatePercent[candidate] = '{:0.2f}%'.format((candidateDic[candidate]/totalCount)*100)
    
    
    voteSummary={}
    vlist = [candidatePercent,candidateDic]
    for k in candidatePercent.keys():
        voteSummary[k]=tuple(voteSummary[k] for voteSummary in vlist)
    

FinalString = f'Total Votes: {totalCount}\n'
FinalString = FinalString + '------------------------\n'
for cRow in voteSummary:
        FinalString = FinalString+f'{cRow}:{voteSummary[cRow][0]} ({voteSummary[cRow][1]}) '
FinalString = FinalString + '\n------------------------\n'
FinalString = f'{FinalString}Winner:{max(candidateDic,key=candidateDic.get)}'
#print(voteSummary)
#print(f'Total Votes: {totalCount}')
#print(candidatePercent)
#print(candidateDic)
print(FinalString)
export = os.path.join("Resources","output.txt")
with open(export,"w") as exportFile:
    exportFile.write(FinalString) 



