import os
import csv

# file path
pybank = os.path.join('Resources','Budget_data.csv')

#define a function, take budget data as its input
def pybank_stat(csvreader, header):

    data = []
    for row in csvreader:
        d = {}
        for i in range(len(header)):
            d[header[i]] = row[i]
        data.append(d)

    change = []
    for i in range(1,len(data)):
        change.append(int(data[i][header[1]])-int(data[i-1][header[1]]))

    profit = [int(data[x][header[1]]) for x in range(len(data))]
    # change = [int(x) for x in change]
    total_month = len(data)
    total_profit = sum(profit)
    ave_change = round(sum(change)/len(change),2)
    max_profit = max(change)
    maxp_index = change.index(max_profit)
    max_loss = min(change)
    maxl_index = change.index(max_loss) 

    print('Financial Analysis')
    print('---------------------------------')
    print(f'Total Months: {total_month}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${ave_change}')
    print(f'Greatest Increase in Profits: {data[maxp_index+1][header[0]]} (${max_profit})')
    print(f'Greatest decrease in Profits: {data[maxl_index+1][header[0]]} (${max_loss})')
      
    with open ('pybank_financial_analysis.txt', 'w') as f:
        print('Financial Analysis', file=f)
        print('---------------------------------', file=f)
        print(f'Total Months: {total_month}', file=f)
        print(f'Total: ${total_profit}', file=f)
        print(f'Average Change: ${ave_change}', file=f)
        print(f'Greatest Increase in Profits: {data[maxp_index+1][header[0]]} (${max_profit})', file=f)
        print(f'Greatest decrease in Profits: {data[maxl_index+1][header[0]]} (${max_loss})', file=f)
        

# Read in the CSV file
with open (pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

    pybank_stat(csvreader, header)

 

