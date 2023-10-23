import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\budget_data.csv")
output_file = os.path.join(dirname, "jh_fin_analysis.txt")


#open csv file
with open(filename, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = "," )
    header = next(csvreader)

    #create index's and set values
    date_ind = header.index("Date")
    profit_loss_ind = header.index("Profit/Losses")

    total_months = 0
    net_total = 0
 
    previous_value = 0
    change = []
    changes_total = 0

    max_increase_value = 0
    max_increase_date = ''
    
    max_decrease_value = 0
    max_decrease_date = ''


    #calculate total months and net total
    for row in csvreader:
        current_month = row[date_ind]
        current_value = int(row[profit_loss_ind])

        net_total += current_value
        total_months += 1

        #find change, average change and max increase and decrease in dataset
        if total_months > 1:
            change = current_value - previous_value
            changes_total += change

            if change > max_increase_value:
                max_increase_value = change
                max_increase_date = current_month

            elif change < max_decrease_value:
                max_decrease_value = change
                max_decrease_date = current_month
        previous_value = current_value

    average_change = round(changes_total / (total_months - 1), 2)

#print results in terminal
print("Financial Analysis")
print("-------------------------")

print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_value})")
      

#print text file
with open (output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------\n")

    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: {net_total}\n")
    text_file.write(f"Average Change: {average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_value})\n")
    text_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_value})")