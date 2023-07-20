import csv
import pandas as pd
from pathlib import Path

#set path to variable not rly necessary but good practice i think
csvfile = Path('PyBank/Resources/budget_data.csv')

#import CSV file
budgetData = pd.read_csv(csvfile)

#Find total number of months included in the dataset
totalmonths = sum(budgetData.Date.value_counts()) 
print("There are " + str(totalmonths) +  " total months")

#Find net total amount of "Profit/Losses" over the entire period
netpnl = sum(budgetData.loc[:, 'Profit/Losses'])
print("Total profit is " + str(netpnl))

#Find the changes in "Profit/Losses" over the entire period, and then the average of those changes
#approach: store profit/loss column in a var and use diff() to get the differences between each row then calculate avg 
differences = budgetData.loc[:, 'Profit/Losses'].diff()

avgchg = round((differences.sum())/differences.count(), 2)
print("Average change is " + str(avgchg))

#The greatest increase in profits (date and amount) over the entire period
#approach: get diff() of profit/loss column and find largest number using max() then get the date 
#to get the date after getting max increase from differences, we have to loop thru original dataframe and check which dates increase equals the largest increase,
#then get the date using locate or something like that

maxincrease = differences.max()
maxIncreaseDateRow = budgetData.loc[:, 'Profit/Losses'].diff().idxmax() #finds row in original csv with max diff in profit loss column
MaxIncreaseDate = budgetData.loc[maxIncreaseDateRow, 'Date']

print("Maximum increase in profit is " + str(maxincrease) + " on " + str(MaxIncreaseDate))

#The greatest decrease in profits (date and amount) over the entire period
maxdecrease = differences.min()

maxDecreaseDateRow = budgetData.loc[:, 'Profit/Losses'].diff().idxmin()
MaxDecreaseDate = budgetData.loc[maxDecreaseDateRow, 'Date']

print("Maximum decrease in profit is " + str(maxdecrease) + " on " + str(MaxDecreaseDate))

#In addition, your final script should both print the analysis to the terminal and export a text file with the results
with open("Analysis.txt", "w") as output:
    print("There are " + str(totalmonths) +  " total months",
          "Total profit is " + str(netpnl),
          "Average change is " + str(avgchg),
          "Maximum increase in profit is " + str(maxincrease) + " on " + str(MaxIncreaseDate), 
          "Maximum decrease in profit is " + str(maxdecrease) + " on " + str(MaxDecreaseDate), file=output)

#a comment about lines 30-52. i can no longer think in a straight procedural line so there is probably a much easier way (like a loop) to do
#the assignment but i could not wrap my mind around it at the moment so this will have to do. it was satisfying to figure out either way.