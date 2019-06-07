import os
import csv
# Specify the path of the file to read
csvpath = os.path.join('election_data.csv')
# Open the file using "read" mode.
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    election = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(election)    

    totalvote = 0  # Create a variable to add up total number of votes
    candidate= []  # Create a wordlist to hold candidates' names
    candidate_count = [] # Create a wordlist to hold no. of candidates' votes
    
    # Read each row of data after the header  
    for row in election:
        # Add 1 to totalvote in each iteration
        totalvote = totalvote +1    
        # Whenever a new name appears add it to the candidate
        if row[2] not in candidate: 
            candidate.append(row[2]) 
     
    # Put zeros in candidate_count, of which the number is the same as that of candidate
    for person in candidate:
        candidate_count.append(0)
    
    # Open the dataset file again using "read" mode.
    with open(csvpath, newline='') as csvfile:
        election = csv.reader(csvfile, delimiter=',')
        csv_header = next(election)
        # Read each row of data after the header
        for row in election:
            # Compare each name in candidate with the name in each row
            # Add 1 to corresponding elements in candidate_count
            for i in range(len(candidate)):
                if row[2] == candidate[i]:
                   candidate_count[i] = candidate_count[i] + 1
    
    # Print the totoal votes, and statistic data of each candidate in terminal
    print("Election Results")
    print("-------------------------------------------------------------------")
    print("Total Votes: " + str(totalvote))
    print("-------------------------------------------------------------------")
    
    # Create a wordlist to hold candidates' statistic data
    result = [] 
    # Compute the % of votes of esch candidate and save it in wordlist percentage
    percentage = ["{0:.3f}".format(number/totalvote*100) + "%" for number in candidate_count]    
    # Creat "list" combine each element of candidate, percentage, and candidate_count
    list = zip(candidate,percentage,candidate_count)
    # Go through the list and print each line to terminal, and save each line as element in result
    for j in list:
        print(j[0] + ": " + j[1] + " (" +str(j[2]) + ")")
        result.append(j[0] + ": " + j[1] + " (" +str(j[2]) + ")")
    print("-------------------------------------------------------------------")
    
    largest = 0 # Create a variable to hold the number of votes of winnter
    winner = [] # Create a wordlist to hold the data of winner
    # Creat "list" combine each element of candidate, percentage, and candidate_count
    list = zip(candidate,percentage,candidate_count)
    # Go through the list,if votes is larger than variable "largest" then update the "largest" with is no. of votes
    # and save this row to winner
    for j in list:
        if j[2] >= largest:
           largest = j[2]
           winner = j
    # Print winner's name
    print("Winner: " + winner[0])
    print("-------------------------------------------------------------------")

# Specify the file to write the result to
output_file = os.path.join("output_pypoll.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w", newline="") as datafile:
    # Initialize csv.writer
    writer = csv.writer(datafile)
    # Write the result line by line to ouput file
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Total Votes: " + str(totalvote)])
    writer.writerow(["-------------------------------------------------------------------"])
    for k in result:
        writer.writerow([k])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Winner: " + winner[0]])
    writer.writerow(["-------------------------------------------------------------------"])
    