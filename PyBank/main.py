import os
import csv
csvpath = os.path.join('dudget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    monthscnt = 0
    total = 0
    profit_loss= []
    month = []
    change = []
    max = ""
    min = ""
    totalchange = 0
       
    for row in budget:
        monthscnt = monthscnt +1
        total = total + int(row[1])
        month.append(row[0])
        profit_loss.append(row[1])
    month.pop(0)
    for i in range(len(profit_loss)-1):
        change.append(int(profit_loss[i+1])-int(profit_loss[i]))
   
    increase = change[0]
    decrease = change[0]
    for mon,cha in zip(month,change):
        if cha >= increase:
           increase = cha
           max = mon  
        if cha <= decrease:
           decrease = cha
           min = mon
        totalchange = totalchange + cha
print("Financial Analysis")
print("-------------------------------------------------------------------")
print("Total Months: " + str(monthscnt))
print("Total: $" + str(int(total)))
print("Average  Change: $" +str( "{0:.2f}".format(totalchange/(monthscnt-1))))
print("Greatest Increase in Profits: " + str(max) + " ($" + str(increase) + ")")
print("Greatest Decrease in Profits: " + str(min)+ " ($" + str(decrease) + ")")

output_file = os.path.join("output_pybank.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Total Months: " + str(monthscnt)])
    writer.writerow(["Total: $" + str(int(total))])
    writer.writerow(["Average  Change: $" +str( "{0:.2f}".format(totalchange/(monthscnt-1)))])
    writer.writerow(["Greatest Increase in Profits: " + str(max) + " ($" + str(increase) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(min)+ " ($" + str(decrease) + ")"])
    