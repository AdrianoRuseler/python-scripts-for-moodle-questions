import csv

# field names 
# username;firstname;lastname;email;password
#fields = ['username', 'firstname', 'lastname', 'email','password'] 
        
# name of csv file 
filename = "userstoimport.csv"
    
# writing to csv file 
with open(filename,newline='\n') as csvfile: 
    # creating a csv writer object 
    csvreader = csv.reader(csvfile,delimiter=';') 
    # This skips the first row of the CSV file.
    next(csvreader) 
    
    for row in csvreader:
        print(row[0])
        print(row[4])
