#library import
import csv

#variable
cvs_file_path=r"C:\Bootcamp\homework\python-challenge\python-challenge\pybank\resources\budget_data.csv"
analisys_folder_file=r"C:\Bootcamp\homework\python-challenge\python-challenge\pybank\analysis\results.txt"
total_number_of_months=0
total=0
day1_income={}
day2_income={}
max_change_income=0
counter=0
day2_max={}
day1_max={}
day2_max_dec={}
day1_max_dec={}
max_decrease_income=-1

#main code
#open file
#with open ('')
print(cvs_file_path)

with open(cvs_file_path, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:

        #print(row['Date'])
        #print(row)
        #to get total months
        total_number_of_months=total_number_of_months+1
        #total profit and loss
        total=total+int(row["Profit/Losses"])
        #skip for first day because there is no previous day
        #sets the next day
        #print(counter)
        if total_number_of_months==1:
            day1_income = row
            day2_income = row
        else:
            day1_income=row
            if max_change_income < (int(day1_income["Profit/Losses"])) - (int(day2_income["Profit/Losses"])):
                max_change_income = (int(day1_income["Profit/Losses"])) - (int(day2_income["Profit/Losses"]))
                day1_max=day1_income
                day2_max=day2_income
            if max_decrease_income > (int(day1_income["Profit/Losses"])) - (int(day2_income["Profit/Losses"])):
                max_decrease_income = (int(day1_income["Profit/Losses"])) - (int(day2_income["Profit/Losses"]))
                day1_max_dec=day1_income
                day2_max_dec=day2_income
            day2_income=row
      

print("total months: " + str(total_number_of_months))
print("total: " + str(total))
print("average change: " + str(total/total_number_of_months))
print("Greatest Increase in Profites: " + day1_max["Date"] +" {" + str(max_change_income) + "}")
print("Greatest Decrease in Profites: " + day1_max_dec["Date"] +" {" + str(max_decrease_income) + "}")


with open(analisys_folder_file, 'w') as filetowrite:
    filetowrite.write("total months: " + str(total_number_of_months))
    filetowrite.write('\n')
    filetowrite.write("total: " + str(total))
    filetowrite.write('\n')
    filetowrite.write("average change: " + str(total/total_number_of_months))
    filetowrite.write('\n')
    filetowrite.write("Greatest Increase in Profites: " + day1_max["Date"] +" {" + str(max_change_income) + "}")
    filetowrite.write('\n')
    filetowrite.write("Greatest Decrease in Profites: " + day1_max_dec["Date"] +" {" + str(max_decrease_income) + "}")
    filetowrite.write('\n')
    filetowrite.write("Thank you for flying colombian airlines")
