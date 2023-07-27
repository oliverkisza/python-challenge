#highlighting entire code and running selected lines in terminal works, unsure why pressing "run" in vsc produces syntax error
import csv
from pathlib import Path

#set csv path
csvpath = Path('python-challenge/PyBank/Resources/budget_data.csv')

with open(csvpath, newline = '') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    #create empty lists for each part
    date = []
    profit = []
    change = []

    #create separate lists for profit and loss columns, convert profit to float for later
    for row in reader:
        profit.append(float(row[1]))
        date.append(row[0])

    #loop thru profit list and subtract current row from prior row, append diff between rows to change list
    for i in range(1, len(profit)):
        change.append(profit[i] - profit[i-1])
        #get dates for min and max profit
        maxdate = date[change.index(max(change))]
        mindate = date[change.index(min(change))]
    
    #take average of change list
    avgchg = sum(change)/(len(profit)-1)

    #print to terminal
    print('Financial Analysis')
    print('---------------------')
    print('Total Months:', len(date))
    print('Total: $', round(sum(profit)))
    print('Average change is ' + str(round(avgchg, 2)))
    print('Greatest Increase in Profits: ' + str(maxdate) + ': ', str(round(max(change))))
    print('Greatest Decrease in Profits: ' + str(mindate) + ': ', str(round(min(change))))

#output to analysis.txt file
with open("Anaylsis.txt", "w") as output:
    print('Financial Analysis', file=output)
    print('---------------------', file=output)
    print('Total Months:', len(date), file=output)
    print('Total: $', round(sum(profit)), file=output)
    print('Average change is ' + str(round(avgchg, 2)), file=output)
    print('Greatest Increase in Profits: ' + str(maxdate) + ': ', str(round(max(change))), file=output)
    print('Greatest Decrease in Profits: ' + str(mindate) + ': ', str(round(min(change))), file=output)