import os
import csv
# Specify the path of the file to read
csvpath = os.path.join('dudget_data.csv')
# Open the file using "read" mode.
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(budget)
       
    monthscnt = 0     # Create a wordlist called monthscnt to hold No. of months
    total = 0         # Create a integer called total to hold total profit
    profit_loss= []   # Create a wordlist to hold profit of each months
    month = []        # Create a wordlist called month to hold name of months
    change = []       # Create a wordlist to hold the profit change between 2 months
    max = ""          # Create a string to hold name of month with greatest increase
    min = ""          # Create a string to hold name of month with greatest decrease
    totalchange = 0   # Create a variable hold total change
    
    # Read each row of dataset after the header   
    for row in budget:
        monthscnt = monthscnt +1    # Add 1 to monthscnt in each iteration
        total = total + int(row[1]) # Add profit to total in each iteration
        month.append(row[0])        # Add name of month to wordlist "month" in each iteration
        profit_loss.append(row[1])  # Add profit to wordlist "profit_loss" in each iteration
    
    # Remove first month from wordlist month, cuz the change cannot be calculated
    month.pop(0)
    # Add the change in profit between 2 continuous months to wordlist "change"
    # So change and month have same number of elements
    for i in range(len(profit_loss)-1):
        change.append(int(profit_loss[i+1])-int(profit_loss[i]))
   
    increase = change[0] # Give increase the value of the profit change between 1st and 2nd month
    decrease = change[0] # Give decrease the value of the profit change between 1st and 2nd month
    # Go through month and change, and save the value to increase whenever a larger change appears
    # ,and save the value to decrease whenever a smaller change appears, and same the name of corresponding month to max and min
    for mon,cha in zip(month,change):
        if cha >= increase:
           increase = cha
           max = mon  
        if cha <= decrease:
           decrease = cha
           min = mon
        # In each iteration add the value of change to totalchange
        totalchange = totalchange + cha

# Print the result to the terminal
print("Financial Analysis")
print("-------------------------------------------------------------------")
# Print the total months of the dataset
print("Total Months: " + str(monthscnt))
# Print the total profit or loss of all the months
print("Total: $" + str(int(total)))
# Print the average change
print("Average  Change: $" +str( "{0:.2f}".format(totalchange/(monthscnt-1))))
# Print the greatest increase in profits among all the months
print("Greatest Increase in Profits: " + str(max) + " ($" + str(increase) + ")")
# Print the greatest decrease in profits among all the months
print("Greatest Decrease in Profits: " + str(min)+ " ($" + str(decrease) + ")")

# Specify the file to write the result to
output_file = os.path.join("output_pybank.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w", newline="") as datafile:
    # Initialize csv.writer
    writer = csv.writer(datafile)
    # Write the result to "output_pybank.csv"
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------------------------------------------"])
    writer.writerow(["Total Months: " + str(monthscnt)])
    writer.writerow(["Total: $" + str(int(total))])
    writer.writerow(["Average  Change: $" +str( "{0:.2f}".format(totalchange/(monthscnt-1)))])
    writer.writerow(["Greatest Increase in Profits: " + str(max) + " ($" + str(increase) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(min)+ " ($" + str(decrease) + ")"])
    