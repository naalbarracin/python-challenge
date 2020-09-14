#library import
import csv

#variable
cvs_file_path=r"C:\Bootcamp\homework\python-challenge\python-challenge\pybank\resources\budget_data.csv"
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
        print(row)
        #to get total months
        total_number_of_months=total_number_of_months+1
        #total profit and loss
        total=total+int(row["Profit/Losses"])
        #skip for first day because there is no previous day
        #sets the next day
        #print(counter)
        if counter==0:
            day1_income=row
            counter=1
            #print(day1_income)
            #print("here")
        #sets the previous day
        else:
            day2_income=row
            #print("me")
            counter=0
            #print("Total"+str((int(day2_income["Profit/Losses"])) - (int(day1_income["Profit/Losses"]))))
            if max_change_income < (int(day2_income["Profit/Losses"])) - (int(day1_income["Profit/Losses"])):
                max_change_income = (int(day2_income["Profit/Losses"])) - (int(day1_income["Profit/Losses"]))
                day1_max=day1_income
                day2_max=day2_income
        print("111111")
        print(day1_income)
        print(day2_income) 
        print("22222")
        if total_number_of_months>1:
            if max_decrease_income > (int(day2_income["Profit/Losses"])) - (int(day1_income["Profit/Losses"])):
                max_decrease_income = (int(day2_income["Profit/Losses"])) - (int(day1_income["Profit/Losses"]))
                day1_max_dec=day1_income
                day2_max_dec=day2_income
                print("1111111111111111111111111")
                print(max_decrease_income)
                #break
                #print(day1_income)
                #print(day2_income) 
           
            
        
        

print("total months: " + str(total_number_of_months))
print("total: " + str(total))
print("average change: " + str(total/total_number_of_months))
print(day2_max["Date"] +" {" + str(max_change_income) + "}")
print(day1_max_dec["Date"] +" {" + str(max_decrease_income) + "}")