from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")

# Question Loop
for _ in range(5):
    quiz.append(ET.Comment('This is a comment'))

    question = ET.SubElement(quiz, "question", type="numerical") # Question Type

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

    GradeOpts=['100','90','83.33333','80','75','70','66.66667','60','50','40','33.33333','30','25','20','16.66667','14.28571','12.5','11.11111','10','5','0']
    # random.choice(GradeOpts)
    answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = str(random.randrange(50,100)) 
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.sentence()
    ET.SubElement(answer,"tolerance").text = str(random.randrange(1,10))

    answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = str(random.randrange(50,100)) 
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.sentence()
    ET.SubElement(answer,"tolerance").text = str(random.randrange(1,10))

    answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = str(random.randrange(50,100)) 
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.sentence()
    ET.SubElement(answer,"tolerance").text = str(random.randrange(1,10))

    answer=ET.SubElement(question, "answer", fraction=random.choice(GradeOpts), format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = str(random.randrange(50,100)) 
    answerfeedback=ET.SubElement(answer, "feedback", format="html") 
    ET.SubElement(answerfeedback,"text").text = fake.sentence()
    ET.SubElement(answer,"tolerance").text = str(random.randrange(1,10))

    hint=ET.SubElement(question,"hint", format="html")
    ET.SubElement(hint,"text").text = fake.catch_phrase()  

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("numericals.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag