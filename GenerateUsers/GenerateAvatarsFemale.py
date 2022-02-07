
import os
import csv
import random
import py_avataaars as pa

# https://github.com/kebu/py-avataaars/blob/master/py_avataaars/__init__.py
SkinColorOpts=['BLACK','PALE','LIGHT','BROWN','DARK_BROWN','PALE','LIGHT']      
HairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED','SILVER_GRAY']
FacialHairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
TopTypeOpts=['HIJAB','TURBAN','WINTER_HAT1','WINTER_HAT2','WINTER_HAT3','WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB','LONG_HAIR_BUN',
            'LONG_HAIR_CURLY','LONG_HAIR_CURVY','LONG_HAIR_FRIDA','LONG_HAIR_FRO','LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
            'LONG_HAIR_MIA_WALLACE','LONG_HAIR_SHAVED_SIDES','LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2','LONG_HAIR_STRAIGHT_STRAND']
FacialHairTypeOpts=['DEFAULT','DEFAULT','DEFAULT']
ClotheTypeOpts=['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
ClotheGraphicTypeOpts=['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','SELENA','BEAR','SKULL_OUTLINE','SKULL']
MouthTypeOpts=['DEFAULT','SERIOUS','SMILE','TWINKLE']
EyesTypeOpts=['DEFAULT','EYE_ROLL','HAPPY','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
EyebrowTypeOpts=['DEFAULT','DEFAULT_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
AccessoriesTypeOpts=['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
HatColorOpts=['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PINK','RED']
ClotheColorOpts=['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PINK','RED']

# name of csv file 
filename = "userstoimportfemale.csv"
if not os.path.isdir('avatars'):
    os.mkdir('avatars')
    
with open(filename,newline='\n',encoding='UTF-8') as csvfile: 
    # creating a csv writer object 
    csvreader = csv.reader(csvfile,delimiter=';') 
    # This skips the first row of the CSV file.
    next(csvreader) 
        
    for row in csvreader:
        RSCO = random.choice(SkinColorOpts)
        RHCO = random.choice(HairColorOpts)
        RTTO = random.choice(TopTypeOpts)
        RFHTO = random.choice(FacialHairTypeOpts)
        RFHCO = random.choice(FacialHairColorOpts)
        RCTO = random.choice(ClotheTypeOpts)
        RCGTO = random.choice(ClotheGraphicTypeOpts)
        RMTO = random.choice(MouthTypeOpts)
        RETO = random.choice(EyesTypeOpts)
        REBTO = random.choice(EyebrowTypeOpts)
        RATO = random.choice(AccessoriesTypeOpts)
        RCCO = random.choice(ClotheColorOpts)
        RHTCO = random.choice(HatColorOpts)
        
        avatar = pa.PyAvataaar(
        style=pa.AvatarStyle.TRANSPARENT,
        skin_color=getattr(pa.SkinColor,RSCO),
        hair_color=getattr(pa.HairColor,RHCO),
        top_type=getattr(pa.TopType,RTTO),
        facial_hair_type=getattr(pa.FacialHairType,RFHTO),
        facial_hair_color=getattr(pa.HairColor,RFHCO),
        clothe_type=getattr(pa.ClotheType,RCTO),
        clothe_graphic_type=getattr(pa.ClotheGraphicType,RCGTO),
        mouth_type=getattr(pa.MouthType,RMTO),
        eye_type=getattr(pa.EyesType,RETO),
        eyebrow_type=getattr(pa.EyebrowType,REBTO),
        accessories_type=getattr(pa.AccessoriesType,RATO),
        clothe_color=getattr(pa.Color,RCCO),
        hat_color=getattr(pa.Color,RHTCO)
        )
        avatar.render_png_file('avatars/'+row[0]+'.png')


# fake.password()
# fake.password()