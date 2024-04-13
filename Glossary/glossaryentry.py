import base64
import requests
from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

na=3 # number of aliases
ne=5 # number of entries
nf=1 # number of attachmentfiles random.choice(["0","1"])
ADDIMG=bool(random.getrandbits(1))

glossary = ET.Element("GLOSSARY")
glossary.append(ET.Comment(fake.catch_phrase())) # This is a comment

# ENTRY Loop
info = ET.SubElement(glossary, "INFO") # glossary info

ET.SubElement(info, "NAME").text = fake.catch_phrase() # glossary name
ET.SubElement(info, "INTRO").text = fake.catch_phrase() # glossary INTRO
ET.SubElement(info, "INTROFORMAT").text = "1" # INTROFORMAT mark 

ET.SubElement(info, "ALLOWDUPLICATEDENTRIES").text = "0" # <ALLOWDUPLICATEDENTRIES>0</ALLOWDUPLICATEDENTRIES>
ET.SubElement(info, "DISPLAYFORMAT").text = "dictionary" # <DISPLAYFORMAT>dictionary</DISPLAYFORMAT>
ET.SubElement(info, "SHOWSPECIAL").text = "1" #   <SHOWSPECIAL>1</SHOWSPECIAL>
ET.SubElement(info, "SHOWALPHABET").text = "1" #  <SHOWALPHABET>1</SHOWALPHABET>
ET.SubElement(info, "SHOWALL").text = "1" # <SHOWALL>1</SHOWALL>
ET.SubElement(info, "ALLOWCOMMENTS").text = "1" # <ALLOWCOMMENTS>0</ALLOWCOMMENTS>
ET.SubElement(info, "USEDYNALINK").text = "1" # <USEDYNALINK>1</USEDYNALINK>
ET.SubElement(info, "DEFAULTAPPROVAL").text = "1" # <DEFAULTAPPROVAL>1</DEFAULTAPPROVAL>
ET.SubElement(info, "GLOBALGLOSSARY").text = "0" #  <GLOBALGLOSSARY>0</GLOBALGLOSSARY>
ET.SubElement(info, "ENTBYPAGE").text = "10" # <ENTBYPAGE>10</ENTBYPAGE>
   
entries = ET.SubElement(info, "ENTRIES") # glossary ENTRIES

# ENTRY LOOP
for e in range(ne):
    entry = ET.SubElement(entries, "ENTRY") # glossary ENTRY
    ET.SubElement(entry, "CONCEPT").text = fake.catch_phrase()# <CONCEPT>Concept</CONCEPT>

    if ADDIMG:
        response = requests.get("https://picsum.photos/200") 
        imgname=(response.headers.get("Content-Disposition").split("filename=")[1]).replace('"', '') 
        imginsert='<p><img src="@@PLUGINFILE@@/'+imgname+'" alt="'+imgname+'"></p>'
        ET.SubElement(entry, "DEFINITION").text = fake.text()+imginsert# <CONCEPT>Concept</CONCEPT>
    else:
        ET.SubElement(entry, "DEFINITION").text = fake.text()# <CONCEPT>Concept</CONCEPT>  

    ET.SubElement(entry, "FORMAT").text = "1" # <FORMAT>1</FORMAT>
    ET.SubElement(entry, "USEDYNALINK").text = "0" # <USEDYNALINK>0</USEDYNALINK>
    ET.SubElement(entry, "CASESENSITIVE").text = "0" # <CASESENSITIVE>0</CASESENSITIVE>
    ET.SubElement(entry, "FULLMATCH").text = "0" # <FULLMATCH>0</FULLMATCH>
    ET.SubElement(entry, "TEACHERENTRY").text = "1" # <TEACHERENTRY>1</TEACHERENTRY>

    eliases = ET.SubElement(entry, "ALIASES") # 
    for a in range(na):
        elias = ET.SubElement(eliases, "ALIAS") #  
        ET.SubElement(elias, "NAME").text = fake.word()#  
     

    if ADDIMG:
        entryfiles = ET.SubElement(entry, "ENTRYFILES") # glossary ENTRY
        efile = ET.SubElement(entryfiles, "FILE") # glossary ENTRY
        # Getting image in bytes
        ET.SubElement(efile, "FILENAME").text = imgname
        ET.SubElement(efile, "FILEPATH").text = '/'#  
        ET.SubElement(efile, "CONTENTS").text = base64.b64encode(response.content).decode("utf-8")
        ET.SubElement(efile, "FILEAUTHOR").text = fake.word()# 
        ET.SubElement(efile, "FILELICENSE").text = fake.word()# 


    attachmentfiles = ET.SubElement(entry, "ATTACHMENTFILES") # glossary ENTRY
    for f in range(nf):
        afile = ET.SubElement(attachmentfiles, "FILE") # glossary ENTRY
        # Getting image in bytes
        aresponse = requests.get("https://picsum.photos/200") 
        ET.SubElement(afile, "FILENAME").text = (aresponse.headers.get("Content-Disposition").split("filename=")[1]).replace('"', '')
        ET.SubElement(afile, "FILEPATH").text = '/'#  
        ET.SubElement(afile, "CONTENTS").text = base64.b64encode(aresponse.content).decode("utf-8")
        ET.SubElement(afile, "FILEAUTHOR").text = fake.word()# 
        ET.SubElement(afile, "FILELICENSE").text = fake.word()# 

    

#ET.SubElement(info, "single").text = random.choice(["True","False"]) # One or multiple answers? 
#ET.SubElement(info, "answernumbering").text = random.choice(["abc","ABCD","123","iii","IIII","none"])
#ET.SubElement(info, "showstandardinstruction").text = random.choice(["0","1"])

tree = ET.ElementTree(glossary)
ET.indent(tree)
tree.write("glossaryentry.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag