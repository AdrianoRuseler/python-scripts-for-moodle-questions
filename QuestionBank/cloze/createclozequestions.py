from faker import Faker # https://faker.readthedocs.io/en/master/#
fake = Faker()
import random
import xml.etree.cElementTree as ET

quiz = ET.Element("quiz")
quiz.append(ET.Comment(fake.catch_phrase())) # This is a comment

# Question Loop
question = ET.SubElement(quiz, "question", type="cloze") # Question Type

# Question Name
name=ET.SubElement(question, "name")
ET.SubElement(name, "text").text = fake.catch_phrase() # Question name 

# Question Text
questiontext=ET.SubElement(question, "questiontext", format="html")

# Question Types
# multiple choice (MULTICHOICE or MC), represented as a dropdown menu in-line in the text,
# multiple choice (MULTICHOICE_V or MCV), represented as a vertical column of radio buttons, or
# multiple choice (MULTICHOICE_H or MCH), represented as a horizontal row of radio-buttons,
MULTICHOICELIST=['MULTICHOICE','MULTICHOICE_H','MULTICHOICE_V','MULTICHOICE_S','MULTICHOICE_HS','MULTICHOICE_VS']

# multiple choice (MULTIRESPONSE or MR), represented as a vertical row of checkboxes
# multiple choice (MULTIRESPONSE_H or MRH), represented as a horizontal row of checkboxes
MULTIRESPONSELIST=['MULTIRESPONSE','MULTIRESPONSE_H','MULTIRESPONSE_S','MULTIRESPONSE_HS']

# numerical answers (NUMERICAL or NM),
# NUMERICALLIST=['NUMERICAL']

# short answers (SHORTANSWER or SA or MW), case is unimportant,
# short answers (SHORTANSWER_C or SAC or MWC), case must match,
SHORTANSWERLIST=['SHORTANSWER','SHORTANSWER_C']

# random select one type
MC=random.choice(MULTICHOICELIST)
MR=random.choice(MULTIRESPONSELIST)
# NM='NUMERICAL'
SA=random.choice(SHORTANSWERLIST)

tmptext = fake.catch_phrase() + " ("+MC+"): {1:" + MC + ":~%100%"+fake.word()+"#"+fake.word()+"~"+fake.word()+"#"+fake.word()+"~"+fake.word()+"#"+fake.word()+"} <br>" # Testing MULTICHOICE
tmptext = tmptext + fake.catch_phrase() + " ("+MR+"): {1:" + MR + ":~"+fake.word()+"#"+fake.word()+"~%50%"+fake.word()+"#"+fake.word()+"~%50%"+fake.word()+"#"+fake.word()+"} <br>" # Testing MULTIRESPONSE
tmptext = tmptext + fake.catch_phrase() + " (NUMERICAL): {1:NUMERICAL:="+str(random.randint(0,1000))+":"+str(random.random())+"#"+fake.word()+"} <br>" # Testing NUMERICAL
tmptext = tmptext + fake.catch_phrase() + " ("+SA+"): {1:" + SA + ":~%100%"+fake.word()+"#"+fake.word()+"} <br>" # Testing SHORTANSWER

ET.SubElement(questiontext,"text").text = tmptext
#ET.SubElement(generalfeedback,"text").text ="<![CDATA["+fake.text()+"]]>" # Como manter o <

generalfeedback=ET.SubElement(question, "generalfeedback", format="html")
ET.SubElement(generalfeedback,"text").text = fake.catch_phrase()  # General feedback 
              
                
ET.SubElement(question, "penalty").text = "0.3333333"
ET.SubElement(question, "hidden").text = "0"
ET.SubElement(question, "idnumber").text = fake.word()

tree = ET.ElementTree(quiz)
ET.indent(tree)
tree.write("cloze.xml",xml_declaration=True, encoding="utf-8",short_empty_elements=True) # Enabled self-closed tag