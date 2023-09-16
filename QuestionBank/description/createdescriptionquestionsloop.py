from faker import Faker
fake = Faker()
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
# Question Loop
for q in range(5):
    quiz.append(ET.Comment("description number: "+str(q+1))) # This is a comment
    question = ET.SubElement(quiz, "question", type="description") # Question Type

    # Question Name
    name=ET.SubElement(question, "name")
    ET.SubElement(name, "text").text = "description "+str(q+1)+': '+fake.catch_phrase()

    # Question Text
    questiontext=ET.SubElement(question, "questiontext", format="html")
    ET.SubElement(questiontext,"text").text = "description "+str(q+1)+";<br>"+fake.text()

    generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
    ET.SubElement(generalfeedback,"text").text = fake.text()

    ET.SubElement(question, "defaultgrade").text = "0"
    ET.SubElement(question, "penalty").text = "0"
    ET.SubElement(question, "hidden").text = "0"
    ET.SubElement(question, "idnumber").text = "description"+str(q+1)

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("descriptions.xml",xml_declaration=True, encoding="utf-8")