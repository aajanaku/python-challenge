import os
import csv

budget_csv = os.path.join(r"C:\Users\aajanaku\OneDrive - Above the Treeline, Inc\Desktop\Resources", "budget_data.csv")

# initialize variables
totalnet = 0
total_months = 0
net_change_list = []

# Open and read csv
with open(budget_csv) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(reader)
    first_row = next(reader)
    total_months += 1
    previous_profitloss = int(first_row[1])
    totalnet = int(first_row[1])
    for row in reader:
        # Track the total
        total_months += 1
        profit_loss = int(row[1])
        totalnet += profit_loss
        net_change = profit_loss - previous_profitloss
        net_change_list.append(net_change)
        previous_profitloss = profit_loss

increase = max(net_change_list)
decrease = min(net_change_list)
average_change = sum(net_change_list) / len(net_change_list)

# Create the result string
results = "Financial Analysis\n"
results += "Total Months: " + str(total_months) + "\n"
results += "Total: $" + str(totalnet) + "\n"
results += "Average Change: $" + str(round(average_change, 2)) + "\n"
results += "Greatest Increase in Profits: $" + str(increase) + "\n"
results += "Greatest Decrease in Profits: $" + str(decrease) + "\n"

# Export results to a text file
with open("results.txt", "w") as file:
    file.write(results)

# Print the results to the console
print(results)




 
