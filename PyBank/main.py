import csv

with open('.//Resources//budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    net_total = 0
    greatest_profit = 0
    greatest_profit_month = 'Dec-00'
    greatest_loss = 0
    greatest_loss_month = 'Dec-00'
    date = 'Dec-00'
    profit_loss = 0
    prev_profit_loss = 0
    for row in csv_reader:
        if line_count > 0:
            date = str(row[0])
            profit_loss = int(row[1])

        net_total += profit_loss
        temp_diff = profit_loss - prev_profit_loss

        if temp_diff > greatest_profit:
            greatest_profit = temp_diff
            greatest_profit_month = date

        if temp_diff < greatest_loss:
            greatest_loss = temp_diff
            greatest_loss_month = date

        prev_profit_loss = profit_loss
        line_count += 1

    print(f'Processed {line_count} lines.')

    num_months = line_count - 1

    file = open(".//analysis/results.txt", "w")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(num_months) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average  Change: $" + "\n")
    file.write("Greatest Increase in Profits: " + greatest_profit_month + " ($" + str(greatest_profit) + ")\n")
    file.write("Greatest Decrease in Profits: " + greatest_loss_month + " ($" + str(greatest_loss) + ")\n")
    file.close()

    print("Financial Analysis\n")
    print("----------------------------\n")
    print("Total Months: " + str(num_months) + "\n")
    print("Total: $" + str(net_total) + "\n")
    print("Average  Change: $" + "\n")
    print("Greatest Increase in Profits: " + greatest_profit_month + " ($" + str(greatest_profit) + ")\n")
    print("Greatest Decrease in Profits: " + greatest_loss_month + " ($" + str(greatest_loss) + ")\n")
    file.close()
