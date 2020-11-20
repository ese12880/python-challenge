import csv

with open('.//Resources//election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    voter_id = ''
    county = ''
    candidate = ''
    x = ''
    v = 0
    candidate_list = []
    candidate_vote = []
    for row in csv_reader:
        if line_count > 0:
            voter_id = str(row[0])
            county = str(row[1])
            candidate = str(row[2])

            if not candidate_list or (candidate not in candidate_list):
                candidate_list.append(candidate)
                candidate_vote.append(1)
            elif candidate in candidate_list:
                candidate_vote[candidate_list.index(candidate)] += 1
        
        line_count += 1
    Total_votes = line_count - 1
    percentage = []

    length = len(candidate_list)
    for i in range(length):
        percentage.append(candidate_vote[i] / Total_votes  * 100)
        if candidate_vote[i] > v:
            v = candidate_vote[i]
            x = candidate_list[i]

    file = open(".//analysis/results2.txt", "w")
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write("Total votes: "  + str(Total_votes) + "\n")
    file.write("----------------------------\n")
    for i in range(length):
        file.write(candidate_list[i] + ": " + str(percentage[i]) + " " + str(candidate_vote[i]) + "\n")
    file.write("----------------------------\n")

    file.write("Winner:" + " " + (x) + "\n")
    
    file.write("----------------------------\n")
    

    file.close()

    print("Election Results")
    print("----------------------------")
    print("total votes:" + str(Total_votes))
    print("-----------------------------")
    for i in range(length):
        print(candidate_list[i] + ": " + str(percentage[i]) + " " + str(candidate_vote[i]))
    print("-----------------------------")
                
    print("Winner:" + " " + (x))
    
    print("-----------------------------")
