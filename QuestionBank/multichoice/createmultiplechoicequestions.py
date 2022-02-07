from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment('This is a comment'))

# Question Loop
question = ET.SubElement(quiz, "question", type="multichoice") # Question Type

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
ET.SubElement(question, "single").text = random.choice(["True","False"]) # One or multiple answers? 
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

GradeOpts=['100','90','83.33333','80','75','70','66.66667','60','50','40','33.33333','30','25','20','16.66667','14.28571','12.5','11.11111','10','5','0']
# random.choice(GradeOpts)
 
answer=ET.SubElement(question, "answer", fraction="75", format="html") 
ET.SubElement(answer,"text").text = fake.sentence()

answer=ET.SubElement(question, "answer", fraction="25", format="html") 
ET.SubElement(answer,"text").text = fake.sentence()

answer=ET.SubElement(question, "answer", fraction="0", format="html") 
ET.SubElement(answer,"text").text = fake.sentence()

answer=ET.SubElement(question, "answer", fraction="0", format="html") 
ET.SubElement(answer,"text").text = fake.sentence()

feedback=ET.SubElement(answer,"feedback", format="html")
ET.SubElement(feedback,"text").text = fake.catch_phrase()

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
tree.write("multichoice.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag