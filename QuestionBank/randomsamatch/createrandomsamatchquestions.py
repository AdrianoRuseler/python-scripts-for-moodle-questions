from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment('This is a comment'))

# Question Loop
question = ET.SubElement(quiz, "question", type="randomsamatch") # Question Type

# Question Name
name=ET.SubElement(question, "name")
ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

# Question Text
questiontext=ET.SubElement(question, "questiontext", format="html")
ET.SubElement(questiontext,"text").text = fake.text() # Question text 

generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
ET.SubElement(generalfeedback,"text").text = fake.text() # General feedback 

ET.SubElement(question, "defaultgrade").text = "1" # Default mark 
ET.SubElement(question, "penalty").text = "0"
ET.SubElement(question, "hidden").text = "0"
ET.SubElement(question, "idnumber").text = fake.word()

correctfeedback=ET.SubElement(question, "correctfeedback", format="html")
ET.SubElement(correctfeedback,"text").text = "Your answer is correct."

partiallycorrectfeedback=ET.SubElement(question, "partiallycorrectfeedback", format="html")
ET.SubElement(partiallycorrectfeedback,"text").text = "Your answer is partially correct."

incorrectfeedback=ET.SubElement(question, "incorrectfeedback", format="html")
ET.SubElement(incorrectfeedback,"text").text = "Your answer is incorrect."

ET.SubElement(question, "choose").text = "2"
ET.SubElement(question, "subcats").text = "1"

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("randomsamatch.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag