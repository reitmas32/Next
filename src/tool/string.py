######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 02/06/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Remove commnets of String
import re
def stripComments(code):
    code = str(code)
    return re.sub(r'(?m)^ *#.*\n?', '', code)

def countWord(text: str, separator:str=" "):
    text_list = text.split(sep=separator)
    return len(text_list)
    
def listToStr(list, separator=None):
    str1 = ""
    for e in list:
        str1 += e
        if separator:
            str1 += separator
    return str1