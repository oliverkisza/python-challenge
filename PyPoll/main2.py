import csv
from pathlib import Path

#set path to var
csvpath = Path('python-challenge/PyPoll/Resources/election_data.csv')

#import CSV
with open(csvpath, newline = '') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

#create empty lists for each part
    ballot_id = []
    counties = []
    candidates = []

    #create separate lists for each column (candidate, county, ballot ID)
    for row in reader:
        ballot_id.append(float(row[0])) #convert ballotID to float in case needed
        counties.append(row[1])
        candidates.append([2])

#Find total number of votes each candidate won

#Find % of vote each candidate won

#Find winner of the election based on popular vote

#print to terminal
    print('Election Results')
    print('---------------------')
    #Total number of votes cast
    print('Total Votes:', len(ballot_id))
    print('---------------------')
    print(candidate, ':', )

    print('Average change is ' + str(round(avgchg, 2)))
    print('Greatest Increase in Profits: ' + str(maxdate) + ': ', str(round(max(change))))
    print('Greatest Decrease in Profits: ' + str(mindate) + ': ', str(round(min(change))))

#output to analysis2.txt file
with open("Anaylsis2.txt", "w") as output:
    print(('Election Results'), file=output)

####################################################################################################

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