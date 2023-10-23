import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\election_data.csv")
output_file = os.path.join(dirname, "jh_vote_analysis.txt")

#open csv file
with open(filename, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ',')
    header = next(csvreader)

    ballot_ind = header.index("Ballot ID")
    county_ind = header.index("County")
    candidate_ind = header.index("Candidate")

    total_votes = 0 
    candidates = {}
    max_votes = 0
    winner = ''
    
    #get total votes 
    for row in csvreader:
        candidate = row[candidate_ind]
        total_votes += 1

        #Get candidates
        if candidate not in candidates:
            candidates[candidate] = 0

        #count votes for for each candidate
        candidates[candidate] +=1

        if candidates[candidate] > max_votes:
            max_votes = candidates[candidate]
            winner = candidate

#print results in terminal, create text file and fine the percentage of votes per candidate
with open (output_file, "w") as text_file:

    print("Election Results")
    print("---------------------\n")

    print(f"Total Votes: {total_votes}")
    print("---------------------\n")

    text_file.write("Election Results\n")
    text_file.write("---------------------\n")

    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("---------------------\n")

    for candidate in candidates:
        votes = candidates[candidate]
        percentage = round(votes/total_votes*100/3)

        print(f"{candidate}: {percentage}% ({candidates[candidate]})")
        text_file.write(f"{candidate}: {percentage}% ({candidates[candidate]})\n")
    print("---------------------\n")

    print(f"Winner:  {winner}")

    print("---------------------")

        
    text_file.write("---------------------\n")

    text_file.write(f"Winner:  {winner}\n")

    text_file.write("---------------------")