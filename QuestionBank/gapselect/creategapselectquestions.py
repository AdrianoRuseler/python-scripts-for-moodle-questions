from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment

# Question Loop
question = ET.SubElement(quiz, "question", type="gapselect") # Question Type

# Question Name
name=ET.SubElement(question, "name")
ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

# 
nquestions=5
qsrt=""
# range(start, stop, step) 
for n in range(1,nquestions+1):
    qsrt=qsrt+fake.sentence()+" [["+str(n)+"]] <br> "

# Question Text
questiontext=ET.SubElement(question, "questiontext", format="html")
ET.SubElement(questiontext,"text").text = qsrt # Question text 

generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
ET.SubElement(generalfeedback,"text").text = fake.text() # General feedback 

ET.SubElement(question, "defaultgrade").text = "1" # Default mark 
ET.SubElement(question, "penalty").text = "0"
ET.SubElement(question, "hidden").text = "0"
ET.SubElement(question, "idnumber").text = fake.word()
ET.SubElement(question, "shuffleanswers").text = random.choice(["True","False"])

correctfeedback=ET.SubElement(question, "correctfeedback", format="html")
ET.SubElement(correctfeedback,"text").text = "Your answer is correct."

partiallycorrectfeedback=ET.SubElement(question, "partiallycorrectfeedback", format="html")
ET.SubElement(partiallycorrectfeedback,"text").text = "Your answer is partially correct."

incorrectfeedback=ET.SubElement(question, "incorrectfeedback", format="html")
ET.SubElement(incorrectfeedback,"text").text = "Your answer is incorrect."

# <shownumcorrect/> self-closed tag
ET.SubElement(question, "shownumcorrect").text = ""

for n in range(1,nquestions+1):
    selectoption=ET.SubElement(question, "selectoption") 
    ET.SubElement(selectoption,"text").text = fake.word()
    ET.SubElement(selectoption,"group").text = str(random.randrange(1,10))

hint=ET.SubElement(question,"hint", format="html")
ET.SubElement(hint,"text").text = fake.catch_phrase()  
# <clearwrong/> self-closed tag
ET.SubElement(hint, "clearwrong").text = ""
# <shownumcorrect/> self-closed tag
ET.SubElement(hint, "shownumcorrect").text = ""

hint=ET.SubElement(question,"hint", format="html")
ET.SubElement(hint,"text").text = fake.catch_phrase()  
# <clearwrong/> self-closed tag
ET.SubElement(hint, "clearwrong").text = ""
# <shownumcorrect/> self-closed tag
ET.SubElement(hint, "shownumcorrect").text = ""


tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("gapselect.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag