from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment('This is a comment'))

# Question Loop
question = ET.SubElement(quiz, "question", type="essay") # Question Type

# Question Name
name=ET.SubElement(question, "name")
ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

# Question Text
questiontext=ET.SubElement(question, "questiontext", format="html")
ET.SubElement(questiontext,"text").text = fake.text() # Question text 

generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
ET.SubElement(generalfeedback,"text").text = fake.text() # General feedback 

ET.SubElement(question, "defaultgrade").text = "1" # Default mark 
ET.SubElement(question, "penalty").text = "0.3333333"
ET.SubElement(question, "hidden").text = "0"
ET.SubElement(question, "idnumber").text = fake.word()
ET.SubElement(question, "responseformat").text = random.choice(["editor","editorfilepicker","plain","monospaced","noinline"])
ET.SubElement(question, "responserequired").text = "1" # Require text 
ET.SubElement(question, "responsefieldlines").text = "10"
ET.SubElement(question, "minwordlimit").text = "50"
ET.SubElement(question, "maxwordlimit").text = "500"
ET.SubElement(question, "attachments").text = "1" # -1 0 1 2 3
ET.SubElement(question, "attachmentsrequired").text = "1" # 0 1 2 3
ET.SubElement(question, "maxbytes").text = "0"
ET.SubElement(question, "filetypeslist").text = "*" # archive,document
  
graderinfo=ET.SubElement(question, "graderinfo", format="html")
ET.SubElement(graderinfo,"text").text = fake.text() # Information for graders

responsetemplate=ET.SubElement(question, "responsetemplate", format="html")
ET.SubElement(responsetemplate,"text").text = fake.text() # Response template


tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("essay.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag