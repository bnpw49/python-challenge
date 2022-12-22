import os
import csv

#Pull data 

PyPollcsv = os.path.join("PyPoll/Resources","election_data.csv")

# Create the lists to store data. 

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []



# Open CSV using the set path PyPollcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # Count the total number of votes and set candidate names to list
        count = count + 1
        
        candidatelist.append(row[2])

        # unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)

        # total number of votes per candidate 
        y = candidatelist.count(x)
        vote_count.append(y)
        
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
      
      #cleanly print outcome to terminal

    print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Print results to txt 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")