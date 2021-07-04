import os
import csv

pyroll = os.path.join('Resources', 'election_data.csv')

def pyroll_stat(csvreader):
    
    cadidates = {}
    total_votes = 0
    for row in csvreader:
        total_votes += 1
        name = row[2]
        if cadidates.get(name, None) is None:
            cadidates[name] = 0
        cadidates[name] += 1
    return cadidates, total_votes 

def printfun(cadidates,total_votes,file_name= None):
    print('Election Results', file=file_name)
    print('--------------------------', file=file_name)
    print(f'Total Votes: {total_votes}', file=file_name)
    print('--------------------------', file=file_name)
    for i in cadidates.keys():
        print(f'{i}: {"{:.3%}".format(cadidates[i]/total_votes)} ({cadidates[i]})', file=file_name)
    print('--------------------------', file=file_name)   
    print(f'{max(cadidates, key=cadidates.get)}: {max(cadidates.values())} ', file=file_name)   

# Read in the CSV file
with open (pyroll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    cad, tv = pyroll_stat(csvreader)
    printfun(cad, tv)

    with open ('election results.txt','w') as f:
        printfun(cad, tv,file_name=f)