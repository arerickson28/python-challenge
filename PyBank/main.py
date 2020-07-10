#Imports
import os
import csv


#csv to read
csvpath = os.path.join( 'Resources', 'budget_data.csv')
#textfile to write
file_to_join = os.path.join('Analysis', "budget_analysis.txt")

#Variables to use
number_of_months = 0 
current_amount = 0
prev_amount = 0
change_in_profit = 0
net_total = 0
avg_change = 0
sum_of_profit_changes = 0
greatest_increase_value = 0
greatest_decrease_value = 0
greatest_increase_month = ""
greatest_decrease_month = ""
message = ""

#Begin writing output message
message = "Financial Analysis" + "\n"
message += "--------------------" + "\n"

#read csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Skip header row
    csv_header = next(csvreader)
    
    #for loop to run on data
    for row in csvreader:
       

        #to count number of months
        number_of_months = number_of_months + 1

        net_total = net_total + int(row[1])

        
        #Calculating Change in profits
        if number_of_months == 1 :
            prev_amount = int(row[1])

        else:
            current_amount = int(row[1])
            change_in_profit = current_amount - prev_amount

            #Identifying greatest decrease
            if  change_in_profit < greatest_decrease_value :
                greatest_decrease_value = change_in_profit
                greatest_decrease_month = row[0]

           #Identifying greatest increase
            if change_in_profit > greatest_increase_value :
                greatest_increase_value = change_in_profit
                greatest_increase_month = row[0]


            #Sum of changes in profit
            prev_amount = current_amount
            sum_of_profit_changes = sum_of_profit_changes  +  change_in_profit

#Average change in profit
avg_change = sum_of_profit_changes / (number_of_months - 1 )

#Finish writing output message
message += "Total Months: " + str(number_of_months) + "\n" 
message += "Total: $" + str(net_total) + "\n"
message += "Average Change: $" + str("{0:.2f}%".format(avg_change)) + "\n"
message += "Greatest Increase in Profits: " + str(greatest_increase_month) + "($" + str(greatest_increase_value) + ")" + "\n"
message += "Greatest Decrease in Profits: " + str(greatest_decrease_month) + "($" + str(greatest_decrease_value) + ")" + "\n"

print(message)


#Export textfile
with open(file_to_join, "w") as txt_file:
    txt_file.write(message)
