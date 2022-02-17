from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")

# Question Loop
for _ in range(10):
    quiz.append(ET.Comment('This is a comment'))

    # Question Loop
    question = ET.SubElement(quiz, "question", type="cloze") # Question Type

    # Question Name
    name=ET.SubElement(question, "name")
    ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

    # Question Text
    questiontext=ET.SubElement(question, "questiontext", format="html")
    ET.SubElement(questiontext,"text").text = fake.text() # Question text 

    generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
    ET.SubElement(generalfeedback,"text").text ="{1:MULTICHOICE:~1#f1~%100%2#f2~%100%3#f3}" #fake.text() # General feedback 
    #ET.SubElement(generalfeedback,"text").text ="<![CDATA["+fake.text()+"]]>" # Como manter o <
                    
    ET.SubElement(question, "penalty").text = "0.3333333"
    ET.SubElement(question, "hidden").text = "0"
    ET.SubElement(question, "idnumber").text = fake.word()

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("clozes.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag