from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")

# Question Loop
for _ in range(5):

    # Is true or false?
    if fake.pybool():
      print("True!")
      qtext=fake.sentence() + ' (True!)'# Question text 
      faf="0"
      taf="100"
    else:
      print("False!")
      qtext=fake.sentence() + ' (False!)'# Question text
      faf="100"
      taf="0"
      
    quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment

    # Question Loop
    question = ET.SubElement(quiz, "question", type="truefalse") # Question Type

    # Question Name
    name=ET.SubElement(question, "name")
    ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

    # Question Text
    questiontext=ET.SubElement(question, "questiontext", format="html")
    ET.SubElement(questiontext,"text").text = qtext # Question text 

    generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
    ET.SubElement(generalfeedback,"text").text = fake.text() # General feedback 

    ET.SubElement(question, "defaultgrade").text = "1" # Default mark 
    ET.SubElement(question, "penalty").text = "1"
    ET.SubElement(question, "hidden").text = "0"
    ET.SubElement(question, "idnumber").text = fake.word()
     
    trueanswer=ET.SubElement(question, "answer", fraction=taf, format="moodle_auto_format") 
    ET.SubElement(trueanswer,"text").text = "true"
    truefeedback=ET.SubElement(trueanswer,"feedback", format="html")
    ET.SubElement(truefeedback,"text").text = fake.catch_phrase()

    falseanswer=ET.SubElement(question, "answer", fraction=faf, format="moodle_auto_format") 
    ET.SubElement(falseanswer,"text").text = "false"
    falsefeedback=ET.SubElement(falseanswer,"feedback", format="html")
    ET.SubElement(falsefeedback,"text").text = fake.catch_phrase()
        
tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("truefalses.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag