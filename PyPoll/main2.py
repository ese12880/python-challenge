import csv

with open('.//Resources//election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    voter_id = ''
    county = ''
    canidate = ''
    canidate_list = []
    canidate_vote = []
    for row in csv_reader:
        if line_count > 0:
            voter_id = str(row[0])
            county = str(row[1])
            canidate = str(row[2])

            if not canidate_list or (canidate not in canidate_list):
                canidate_list.append(canidate)
                canidate_vote.append(1)
            elif canidate in canidate_list:
                canidate_vote[canidate_list.index(canidate)] += 1
        
        line_count += 1


    file = open(".//analysis/results2.txt", "w")
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write("Total votes: "  + "\n")
    file.write("----------------------------\n")
    #file.write( + str(canidate_list) + "\n")
    
    #file.write(")
    #file.write(
    #file.write(
    file.close()

    print("Election Results\n")
    print("----------------------------\n")
    print("total votes:")
    print("-----------------------------\n")
    #print("Total Months: " + str(num_months) + "\n")
    #print("Total: $" + str(net_total) + "\n")
    #print("Average  Change: $" + "\n")
    #print("Greatest Increase in Profits: " + greatest_profit_month + " ($" + str(greatest_profit) + ")\n")
    #print("Greatest Decrease in Profits: " + greatest_loss_month + " ($" + str(greatest_loss) + ")\n")
   
    print(f'Processed {line_count} lines.')
