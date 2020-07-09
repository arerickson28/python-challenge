import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0

candidates = {
    
}


# khan_count = 0
# correy_count = 0
# li_count = 0
# otool_count = 0

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




#         if row[2] == "Khan" :
#             khan_count = khan_count + 1

#         if row[2] == "Correy" :
#             correy_count = correy_count +1

#         if row[2] == "Li" :
#             li_count = li_count + 1

#         if row[2] == "O'Tooley" :
#             otool_count = otool_count + 1

print(total_votes)
# print(khan_count)
# print(correy_count)
# print(li_count)
# print(otool_count)

for candidate_name, vote_count in candidates.items() :
    print(f'{candidate_name}: {vote_count}')


print(candidates)