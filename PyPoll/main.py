import os
import csv

election_data_csv = "election_data.csv"


# 1 - instantiate variables (create and set to 0) 
total_votes = 0
khan_total = 0 
#khan_stats 
correy_total = 0
#correy_stats
li_total= 0
#li_stats 
otooley_total = 0
#otooley_stats 
candidate = []


with open(election_data_csv) as election_data: 
    reader = csv.DictReader(election_data, delimiter=",")

    # 2 - iterate throough votes
    for row in reader:
        total_votes = int(total_votes) + 1

        votes_cast = str(row["Candidate"])
        if votes_cast == "Khan": 
            khan_total = khan_total + 1
        
        if votes_cast == "Correy":
            correy_total = correy_total + 1
        
        if votes_cast == "Li": 
            li_total = li_total + 1
        
        if votes_cast == "O'Tooley":
            otooley_total = otooley_total + 1
        
khan_stats = (khan_total/total_votes) *100
correy_stats = (correy_total/total_votes) *100
li_stats = (li_total/total_votes) *100
otooley_stats = (otooley_total/total_votes) *100

max_candidate = 0 
candidate_vote_dict = {khan_total: "Khan", correy_total: "Correy", 
                        li_total: "Li", otooley_total: "O'Tooley"}
candidate_vote_list = [khan_total, correy_total, li_total, otooley_total]

for candidate in candidate_vote_list:
    if candidate > max_candidate:
        max_candidate = candidate

f = open("election_data.txt", "w+")

# Election Results
print("Election Results")
print("-------------------------") 
f.write("Election Results"+ "\n")
f.write("-------------------------"+ "\n")

# # Total Votes: 3521001
print("Total Votes: " +  str(total_votes))
print("-------------------------")
f.write("Total Votes: " +  str(total_votes))
f.write("-------------------------"+ "\n")

# Khan: 63.000% (2218231)
print("Khan: " + str(khan_stats) + "% " + (str(khan_total)))
f.write("Khan: " + str(khan_stats) + "% " + (str(khan_total))+ "\n")

# Correy: 20.000% (704200)
print("Correy: " + str(correy_stats) + "% " + (str(correy_total)))
f.write("Correy: " + str(correy_stats) + "% " + (str(correy_total))+ "\n")

# Li: 14.000% (492940)
print("Li: " + str(li_stats) + "% " + (str(li_total)))
f.write("Li: " + str(li_stats) + "% " + (str(li_total))+ "\n")

#  O'Tooley: 3.000% (105630)
print("O'Tooley: " + str(otooley_stats) + "% " + (str(otooley_total)))
print("-------------------------")
f.write("O'Tooley: " + str(otooley_stats) + "% " + (str(otooley_total)) + "\n")
f.write("-------------------------" + "\n")

#  Winner: Khan

print("Winner: " + str(candidate_vote_dict[max_candidate]))
print("-------------------------")
f.write("Winner: " + str(candidate_vote_dict[max_candidate]) +"\n")
f.write("-------------------------" + "\n")

f.close()
