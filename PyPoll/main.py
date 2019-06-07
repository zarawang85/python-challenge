import os
import csv
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election = csv.reader(csvfile, delimiter=',')
    csv_header = next(election)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    totalvote = 0
    candidate= []
    candidate_count = []
      
    for row in election:
        totalvote = totalvote +1
        if row[2] not in candidate:
            candidate.append(row[2])
     
    count = 0
    candidate_count = []
    for person in candidate:
        candidate_count.append(0)
    with open(csvpath, newline='') as csvfile:
        election = csv.reader(csvfile, delimiter=',')
        csv_header = next(election)
        for row in election:
            for i in range(len(candidate)):
                if row[2] == candidate[i]:
                   candidate_count[i] = candidate_count[i] + 1
    
    result = []
    percentage = ["{0:.3f}".format(number/totalvote*100) + "%" for number in candidate_count]
    print("Election Results")
    print("-------------------------------------------------------------------")
    print("Total Votes: " + str(totalvote))
    print("-------------------------------------------------------------------")
    list = zip(candidate,percentage,candidate_count)
    for j in list:
        print(j[0] + ": " + j[1] + " (" +str(j[2]) + ")")
        result.append(j[0] + ": " + j[1] + " (" +str(j[2]) + ")")
    print("-------------------------------------------------------------------")
    largest = 0
    winner = []
    list = zip(candidate,percentage,candidate_count)
    for j in list:
        if j[2] >= largest:
           largest = j[2]
           winner = j
    print("Winner: " + winner[0])
    print("-------------------------------------------------------------------")

output_file = os.path.join("output_pypoll.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Total Votes: " + str(totalvote)])
    writer.writerow(["-------------------------------------------------------------------"])
    for k in result:
        writer.writerow([k])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Winner: " + winner[0]])
    writer.writerow(["-------------------------------------------------------------------"])
    