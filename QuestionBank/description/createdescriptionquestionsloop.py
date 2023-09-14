from faker import Faker
fake = Faker()
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
# Question Loop
for _ in range(10):
    quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment
    question = ET.SubElement(quiz, "question", type="description") # Question Type

    # Question Name
    name=ET.SubElement(question, "name")
    ET.SubElement(name, "text").text = fake.catch_phrase()

    # Question Text
    questiontext=ET.SubElement(question, "questiontext", format="html")
    ET.SubElement(questiontext,"text").text = fake.text()

    generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
    ET.SubElement(generalfeedback,"text").text = fake.text()

    ET.SubElement(question, "defaultgrade").text = "0"
    ET.SubElement(question, "penalty").text = "0"
    ET.SubElement(question, "hidden").text = "0"
    ET.SubElement(question, "idnumber").text = fake.word()

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("descriptions.xml",xml_declaration=True, encoding="utf-8")