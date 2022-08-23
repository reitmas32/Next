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

def jsonObjKey(json_obj):
    for key in json_obj:
        return key
    
def jsonObjValue(json_obj):
    for key in json_obj:
        value = json_obj[key]
        return value