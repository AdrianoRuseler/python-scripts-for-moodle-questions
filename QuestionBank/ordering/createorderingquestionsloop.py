from faker import Faker
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")

# Question Loop
for _ in range(10):
    quiz.append(ET.Comment('This is a comment'))
    question = ET.SubElement(quiz, "question", type="ordering") # Question Type

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
    ET.SubElement(question, "layouttype").text = random.choice(["VERTICAL","HORIZONTAL"]) # One or multiple answers? 
    ET.SubElement(question, "selecttype").text = random.choice(["ALL","RANDOM","CONTIGUOUS"])
    ET.SubElement(question, "selectcount").text = "0" # 0->Todos
    ET.SubElement(question, "gradingtype").text = random.choice(["ABSOLUTE_POSITION","ALL_OR_NOTHING","RELATIVE_TO_CORRECT","RELATIVE_NEXT_EXCLUDE_LAST","RELATIVE_NEXT_INCLUDE_LAST","RELATIVE_ONE_PREVIOUS_AND_NEXT","RELATIVE_ALL_PREVIOUS_AND_NEXT","LONGEST_ORDERED_SUBSET","LONGEST_CONTIGUOUS_SUBSET"])
    ET.SubElement(question, "showgrading").text = random.choice(["SHOW","HIDE"])
    ET.SubElement(question, "numberingstyle").text = random.choice(["abc","ABCD","123","iii","IIII","none"])

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
     
    answer=ET.SubElement(question, "answer", fraction="1", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()
    answer=ET.SubElement(question, "answer", fraction="2", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()
    answer=ET.SubElement(question, "answer", fraction="3", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()
    answer=ET.SubElement(question, "answer", fraction="4", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()
    answer=ET.SubElement(question, "answer", fraction="5", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()
    answer=ET.SubElement(question, "answer", fraction="6", format="moodle_auto_format") 
    ET.SubElement(answer,"text").text = fake.catch_phrase()


    feedback=ET.SubElement(answer,"feedback", format="html")
    ET.SubElement(feedback,"text").text = fake.catch_phrase()

    hint=ET.SubElement(question,"hint", format="html")
    ET.SubElement(hint,"text").text = fake.catch_phrase()  

    hint=ET.SubElement(question,"hint", format="html")
    ET.SubElement(hint,"text").text = fake.catch_phrase()  


tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("orderings.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag