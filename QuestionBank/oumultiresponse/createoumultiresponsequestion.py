from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")


quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment
# Question Loop
question = ET.SubElement(quiz, "question", type="oumultiresponse") # Question Type

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
ET.SubElement(question, "shuffleanswers").text = random.choice(["True","False"])
ET.SubElement(question, "answernumbering").text = random.choice(["abc","ABCD","123","iii","IIII","none"])
ET.SubElement(question, "showstandardinstruction").text = random.choice(["0","1"])

correctfeedback=ET.SubElement(question, "correctfeedback", format="html")
ET.SubElement(correctfeedback,"text").text = "Your answer is correct."

partiallycorrectfeedback=ET.SubElement(question, "partiallycorrectfeedback", format="html")
ET.SubElement(partiallycorrectfeedback,"text").text = "Your answer is partially correct."

incorrectfeedback=ET.SubElement(question, "incorrectfeedback", format="html")
ET.SubElement(incorrectfeedback,"text").text = "Your answer is incorrect."

# <shownumcorrect/> self-closed tag
ET.SubElement(question, "shownumcorrect").text = ""

GradeOpts=['100','0']
# random.choice(GradeOpts)
 
answer=ET.SubElement(question, "answer", fraction="100", format="html") 
ET.SubElement(answer,"text").text = fake.catch_phrase()
feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()

answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="html") 
ET.SubElement(answer,"text").text = fake.catch_phrase()
feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()

answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="html") 
ET.SubElement(answer,"text").text = fake.catch_phrase()
feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()

answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="html") 
ET.SubElement(answer,"text").text = fake.catch_phrase()
feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()

answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="html") 
ET.SubElement(answer,"text").text = fake.catch_phrase()
feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()


tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("oumultiresponse.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag