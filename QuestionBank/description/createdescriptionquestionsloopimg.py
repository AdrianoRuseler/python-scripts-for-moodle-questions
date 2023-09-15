import base64
import requests
from faker import Faker
fake = Faker()
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
# Question Loop
for q in range(5):
    quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment

    # Question Loop
    question = ET.SubElement(quiz, "question", type="description") # Question Type

    # Question Name
    name=ET.SubElement(question, "name")
    ET.SubElement(name, "text").text = fake.catch_phrase()

    # Question Text
    questiontext=ET.SubElement(question, "questiontext", format="html")


    #name="839-200x200.jpg" path="/" encoding="base64"
    # Getting image in bytes
    response = requests.get("https://picsum.photos/200") 
    imgname=(response.headers.get("Content-Disposition").split("filename=")[1]).replace('"', '') 
    imginsert='<p><img class="img-fluid align-top" src="@@PLUGINFILE@@/'+imgname+'" alt="'+fake.catch_phrase()+'" width="200" height="200"></p>'

    ET.SubElement(questiontext,"text").text = fake.text()+imginsert
    ET.SubElement(questiontext,"file",name=imgname.strip(),path="/",encoding="base64").text = base64.b64encode(response.content).decode("utf-8")

    generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
    ET.SubElement(generalfeedback,"text").text = fake.text()

    ET.SubElement(question, "defaultgrade").text = "0"
    ET.SubElement(question, "penalty").text = "0"
    ET.SubElement(question, "hidden").text = "0"
    ET.SubElement(question, "idnumber").text = fake.word()

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("descriptionloopimg.xml",xml_declaration=True, encoding="utf-8")