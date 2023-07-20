import csv
import pandas as pd
from pathlib import Path

#set path to var
csvfile = Path('PyPoll/Resources/election_data.csv')

#import CSV
electionData = pd.read_csv(csvfile)

#Find total number of votes cast
totalVotes = sum(electionData.value_counts())
print(str(totalVotes) + ' total votes')

#make a complete list of candidates who received votes
votedCandidates = electionData.copy()
votedCandidateList = votedCandidates.Candidate.unique()

#The total number of votes each candidate won
candidateVoteSums = votedCandidates['Candidate'].value_counts()
print(candidateVoteSums)

#The percentage of votes each candidate won 
candidate0percent = ((candidateVoteSums[0]/totalVotes)*100).round(3)
print(votedCandidateList[0] + ': ' + str(candidate0percent) + '%')

candidate1percent = ((candidateVoteSums[1]/totalVotes)*100).round(3)
print(votedCandidateList[1] + ': ' + str(candidate1percent) + '%')

candidate2percent = ((candidateVoteSums[2]/totalVotes)*100).round(3)
print(votedCandidateList[2] + ': ' + str(candidate2percent) + '%')

#The winner of the election based on popular vote
#this is an extremely obtuse way of doing this but since i didnt use a loop above (i forgot they existed) this is my way of not rewriting everything
candidateList = [candidate0percent, candidate1percent, candidate2percent]
winnerNum = max(candidateList)
if winnerNum == candidate0percent:
    winner = 'Diana DeGette'
    print('Winner is Diana DeGette!')

if winnerNum == candidate1percent:
    winner = 'Charles Casper Stockham'
    print('Winner is Charles Casper Stockham!')

if winnerNum == candidate2percent:
    winner = 'Anthony Doane'
    print('Winner is Anthony Doane!')

#export to text file
with open("Analysis2.txt", "w") as output:
    print(str(totalVotes) + ' total votes',
          candidateVoteSums,
          print(votedCandidateList[0] + ': ' + str(candidate0percent) + '%'),
          print(votedCandidateList[1] + ': ' + str(candidate1percent) + '%'),
          print(votedCandidateList[2] + ': ' + str(candidate2percent) + '%'),
          print('Winner is ' + str(winner) + '!'),
          file=output)