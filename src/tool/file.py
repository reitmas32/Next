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

def remplace_in_file(file_location, old_text, new_text):
    try:
        #input file
        fin = open(file_location, "rt")

        old_data = fin.readlines()

        new_data = ""

        #for each line in the input file
        for line in old_data:
            #read replace the string and write to output file
            new_data += line.replace(old_text, new_text)
        #close input and output files
        fin.close()

        #output file to write the result to
        fout = open(file_location, "wt")

        #Write new data
        fout.write(new_data)

        #Close output file
        fout.close()
    except BaseException as err:
        print("Not remplace " + old_text + " in " + file_location)
        print(f"Unexpected {err=}, {type(err)=}")