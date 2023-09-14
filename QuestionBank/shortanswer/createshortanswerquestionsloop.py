from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment

nq=10
# Question Loop
for _ in range(nq):
    question = ET.SubElement(quiz, "question", type="shortanswer") # Question Type

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
    ET.SubElement(question, "usecase").text = random.choice(["0","1"]) # Case sensitivity 

    answer=ET.SubElement(question, "answer", fraction="100", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.sentence()
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.catch_phrase()

    answer=ET.SubElement(question, "answer", fraction="25", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.sentence()
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.catch_phrase()

    answer=ET.SubElement(question, "answer", fraction="0", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.sentence()
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.catch_phrase()

    answer=ET.SubElement(question, "answer", fraction="0", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.sentence()
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.catch_phrase()

    hint=ET.SubElement(question,"hint", format="html")
    ET.SubElement(hint,"text").text = fake.catch_phrase()  
    # <clearwrong/> self-closed tag
    #ET.SubElement(hint, "clearwrong").text = ""
    # <shownumcorrect/> self-closed tag
    #ET.SubElement(hint, "shownumcorrect").text = ""


tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("shortanswers.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag