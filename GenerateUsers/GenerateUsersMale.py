# Faker is a Python package that generates fake data for you.
from faker import Faker
fake = Faker()
# fake = Faker('pt_BR')

import csv

# field names 
# username;firstname;lastname;email;password
fields = ['username', 'firstname', 'lastname', 'email','password'] 
        
# name of csv file 
filename = "userstoimportmale.csv"
    
# writing to csv file 
with open(filename, 'w',newline='\n') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile,delimiter=';') 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    for _ in range(100):
        fname=fake.first_name_male()
        lname=fake.last_name()
        username=str.lower(fname+lname)
        email=username+"@"+fake.domain_name()
        csvwriter.writerows([[username,fname,lname,email,fake.password()]])
# fake.password()
# fake.password()