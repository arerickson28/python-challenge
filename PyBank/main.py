#dependencies
import os
import csv

#open file and load

csvpath = os.path.join( 'Resources', 'budget_data.csv')

#output to file



#Financial Parameters
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
#Read the csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
#     #extract first row to avoid appending to net_change_list
        #first_row =

    # Read each row of data after the header
    for row in csvreader:
        #print(row)

#         #track total
        number_of_months = number_of_months + 1

        net_total = net_total + int(row[1])
#         #track net change
        

        if number_of_months == 1 :
            prev_amount = int(row[1])

        else:
            current_amount = int(row[1])
            change_in_profit = current_amount - prev_amount

            if  change_in_profit < greatest_decrease_value :
                greatest_decrease_value = change_in_profit
                greatest_decrease_month = row[0]
           
            if change_in_profit > greatest_increase_value :
                greatest_increase_value = change_in_profit
                greatest_increase_month = row[0]



            prev_amount = current_amount
            sum_of_profit_changes = sum_of_profit_changes  +  change_in_profit


avg_change = sum_of_profit_changes / (number_of_months - 1 )
#  #Generate the output
#  output = 

#  #print output
#  print(output)

#  #export the results to textfile

message = str(number_of_months) + "\n" 
message += str(net_total) + "\n"

print(number_of_months)
print(net_total)
print(avg_change)
print(greatest_decrease_month)
print(greatest_decrease_value)
print(greatest_increase_month)
print(greatest_increase_value)

print(message)



file_to_join = os.path.join('Analysis', "budget_analysis.txt")

with open(file_to_join, "w") as txt_file:
    txt_file.write(message)
