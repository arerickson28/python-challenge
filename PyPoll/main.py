import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0

candidates = {}
message = ""


with open(file_to_load) as election_data :
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1

        name = row[2]

        if name not in candidates :
            candidates[name] = 1

        else:
            candidates[name] = candidates[name] + 1





message = "Election Results" + "\n"
message += "Total Votes: " + str(total_votes) + "\n"


for candidate_name, vote_count in candidates.items() :
    percentage = "{0:.3f}%".format(( vote_count / total_votes ) * 100)
    
    winner = max(candidates, key=candidates.get)

    results = (f'{candidate_name}: {vote_count}, {percentage}')
    message += results + "\n"

message += "Winner: " + winner
print(message)



with open(file_to_output, "w") as txt_file:
    txt_file.write(message)
