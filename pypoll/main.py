#library import
import csv

#variable
cvs_file_path=r"C:\Bootcamp\02-Python (1)\02-Python\Instructions\PyPoll\Resources\election_data.csv"
analisys_folder_file=r"C:\Bootcamp\homework\python-challenge\python-challenge\PyPoll\analysis\results.txt"

total_votes = 0
candidates=[]
votes=[0,0,0,0]

with open(cvs_file_path, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        total_votes=total_votes+1
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"]) 
        if row["Candidate"]=="Khan":
            votes[0]=votes[0]+1
        if row["Candidate"]=="Correy":
            votes[1]=votes[1]+1
        if row["Candidate"]=="Li":
            votes[2]=votes[2]+1  
        if row["Candidate"]=="O'Tooley":
            votes[3]=votes[3]+1       
           

print("Election Results")
print("------------")
print("Total Votes: " + str(total_votes))
print("------------")
print(str(candidates[0]) + ": " + str(votes[0]/total_votes*100) +"% (" + str(votes[0]) + ")" )
print(str(candidates[1]) + ": " + str(votes[1]/total_votes*100) +"% (" + str(votes[1]) + ")" )
print(str(candidates[2]) + ": " + str(votes[2]/total_votes*100) +"% (" + str(votes[2]) + ")" )
print(str(candidates[3]) + ": " + str(votes[3]/total_votes*100) +"% (" + str(votes[3]) + ")" )
print("------------")


if (votes.index(max(votes)))==0:
    print("winner: khan")
if (votes.index(max(votes)))==1: 
     print("winner: correy")
if (votes.index(max(votes)))==2:
    print("winner: li")   
if (votes.index(max(votes)))==3:
    print("winner: o'toley")         
print("------------")

with open(analisys_folder_file, 'w') as filetowrite:
    filetowrite.write("Election Results")
    filetowrite.write('\n')
    filetowrite.write("------------")
    filetowrite.write('\n')
    filetowrite.write("Total Votes: " + str(total_votes))
    filetowrite.write('\n')
    filetowrite.write("------------")
    filetowrite.write('\n')
    filetowrite.write(str(candidates[0]) + ": " + str(votes[0]/total_votes*100) +"% (" + str(votes[0]) + ")" )
    filetowrite.write('\n')
    filetowrite.write(str(candidates[1]) + ": " + str(votes[1]/total_votes*100) +"% (" + str(votes[1]) + ")" )
    filetowrite.write('\n')
    filetowrite.write(str(candidates[2]) + ": " + str(votes[2]/total_votes*100) +"% (" + str(votes[2]) + ")" )
    filetowrite.write('\n')
    filetowrite.write(str(candidates[3]) + ": " + str(votes[3]/total_votes*100) +"% (" + str(votes[3]) + ")" )
    filetowrite.write('\n')
    filetowrite.write("------------")
    filetowrite.write('\n')

    if (votes.index(max(votes)))==0:
        filetowrite.write("winner: khan")
    if (votes.index(max(votes)))==1: 
        filetowrite.write("winner: correy")
    if (votes.index(max(votes)))==2:
        filetowrite.write("winner: li")   
    if (votes.index(max(votes)))==3:
        filetowrite.write("winner: o'toley")  
    filetowrite.write('\n')

    filetowrite.write("------------")

