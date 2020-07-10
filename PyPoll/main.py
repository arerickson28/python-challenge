#Imports
import os
import csv

#cvs to read
file_to_load = os.path.join("Resources", "election_data.csv")

#textfile to write
file_to_output = os.path.join("Analysis", "election_analysis.txt")

#variables to use
total_votes = 0

candidates = {}
message = ""

#Read csv
with open(file_to_load) as election_data :
    reader = csv.reader(election_data)

    header = next(reader)

#For loop to count votes 
    for row in reader:

        total_votes = total_votes + 1

        name = row[2]

        #If statement to populate dictionary
        if name not in candidates :
            candidates[name] = 1

        else:
            candidates[name] = candidates[name] + 1

#Begin writing output message
message = "Election Results" + "\n"
message += "--------------------" + "\n"
message += "Total Votes: " + str(total_votes) + "\n"
message += "--------------------" + "\n"


#To find percent of vote for each candidate and to determine winner
for candidate_name, vote_count in candidates.items() :
    percentage = "{0:.3f}%".format(( vote_count / total_votes ) * 100)
    
    winner = max(candidates, key=candidates.get)

    results = (f'{candidate_name}: {vote_count}, {percentage}')

    #Add to output message
    message += results + "\n"

#Finish writing output message
message += "--------------------" + "\n"
message += "Winner: " + winner + "\n" + "---------------------"
print(message)


#Export textfile
with open(file_to_output, "w") as txt_file:
    txt_file.write(message)
