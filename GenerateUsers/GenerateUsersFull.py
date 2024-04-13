# Faker is a Python package that generates fake data for you.
from faker import Faker
fake = Faker()
# fake = Faker('pt_BR')

import csv

# name of csv file 
filename = "userstoimportfull.csv"
nusers = 5

# field names 
# username;firstname;lastname;email;password
fields = ['username', 'firstname', 'lastname', 'email','password'] 
# https://docs.moodle.org/404/en/Upload_users
      

# writing to csv file 
with open(filename, 'w',newline='\n') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile,delimiter=';') 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    for _ in range(nusers):
        fname=fake.first_name()
        lname=fake.last_name()
        username=str.lower(fname+lname)
        email=username+"@"+fake.domain_name()
        csvwriter.writerows([[username,fname,lname,email,fake.password()]])
# fake.password()
# fake.password()