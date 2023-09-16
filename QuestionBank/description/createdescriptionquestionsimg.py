import base64
import requests
from faker import Faker
fake = Faker()
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
q=0 # Question number
quiz.append(ET.Comment("description quiz type number: "+str(q+1))) # This is a comment

# Question Loop
question = ET.SubElement(quiz, "question", type="description") # Question Type

# Question Name
name=ET.SubElement(question, "name")
ET.SubElement(name, "text").text = "description "+str(q+1)+': '+fake.catch_phrase()

# Question Text
questiontext=ET.SubElement(question, "questiontext", format="html")

# Getting image in bytes
response = requests.get("https://picsum.photos/200") 
imgname=(response.headers.get("Content-Disposition").split("filename=")[1]).replace('"', '') 
imginsert='<p><img class="img-fluid align-top" src="@@PLUGINFILE@@/'+imgname+'" alt="'+fake.catch_phrase()+'" width="200" height="200"></p>'

ET.SubElement(questiontext,"text").text = fake.text()+imginsert
ET.SubElement(questiontext,"file",name=imgname.strip(),path="/",encoding="base64").text = base64.b64encode(response.content).decode("utf-8")

generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
# Getting image in bytes
response = requests.get("https://picsum.photos/200") 
imgname=(response.headers.get("Content-Disposition").split("filename=")[1]).replace('"', '') 
imginsert='<p><img class="img-fluid align-top" src="@@PLUGINFILE@@/'+imgname+'" alt="'+fake.catch_phrase()+'" width="200" height="200"></p>'

ET.SubElement(generalfeedback,"text").text = fake.text()+imginsert
ET.SubElement(generalfeedback,"file",name=imgname.strip(),path="/",encoding="base64").text = base64.b64encode(response.content).decode("utf-8")

ET.SubElement(question, "defaultgrade").text = "0"
ET.SubElement(question, "penalty").text = "0"
ET.SubElement(question, "hidden").text = "0"
ET.SubElement(question, "idnumber").text = "description"+str(q+1)

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("descriptionimg.xml",xml_declaration=True, encoding="utf-8")