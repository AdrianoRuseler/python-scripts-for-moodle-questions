# Faker is a Python package that generates fake data for you.
from faker import Faker

fake = Faker()
        
# name of txt file 
filename = "userstoimportx.ldif"
nusers = 2
# writing to txt file 
f = open(filename, "w")
f.write("version: 1\n\n")
        
        
allou="dn: ou=all,dc=server,dc=local\nobjectClass: organizationalUnit\nobjectClass: top\nou: all\n\n"
f.write(allou)

# groups = ["students", "teachers", "mdlmanager", "mdlcoursecreator"]
nusersgroup= [5,2,1,1] # number os users per group
# campus = ["ap", "cm", "cp", "ct","dv","fb","gp","ld","md","pb","pg","rt","sh","td"] 

groups = ["students", "teachers"]
campus = ["ap", "ct"] 

for x in groups:
    groupsou="dn: ou="+x+",ou=all,dc=server,dc=local\nobjectClass: organizationalUnit\nobjectClass: top\nou: "+x+"\n\n"
    f.write(groupsou)
    
    for y in campus:
        groupsou="dn: ou="+y+",ou="+x+",ou=all,dc=server,dc=local\nobjectClass: organizationalUnit\nobjectClass: top\nou: "+y+"\n\n"
        f.write(groupsou)


for x in groups:    
    for y in campus:
        for _ in range(nusers):
            fname=fake.first_name()
            lname=fake.last_name()
            nome=fname+" "+lname
            username=str.lower(fname+lname)
            email=username+"@"+fake.domain_name()
            userpass=fake.password()
            #cidade=faker.city()
            emprego=fake.job()
            
            useruid="dn: uid="+username+",ou="+y+",ou="+x+",ou=all,dc=server,dc=local\nobjectClass: inetOrgPerson\nobjectClass: organizationalPerson\nobjectClass: person\nobjectClass: top\n"
            f.write(useruid)
            userstr="cn: "+fname+"\nsn: "+lname+"\ngivenName: "+nome+"\nuid: "+username+"\nuserPassword: "+userpass+"\nmail: "+email+"\nl: "+y+"\n\n"
            f.write(userstr)        
f.close()        
        
# fake.password()
# fake.password()

  

# fake.address()