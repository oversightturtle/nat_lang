verbose = True

def v_p(txt):
    if verbose == True:
        print(txt)

v_p("_INIT >> IMPORT SPACY")

import spacy

v_p("FINSH IMPORT // LOADING EN")

nlp = spacy.load("en")

v_p("LOADED EN // START TXT IMPORT")

doc = open("input-custom.txt").read()

v_p("LOADED FILE // STARTING NLP")

doc = nlp(doc)

v_p("NLP DONE ... ")

for token in doc:
    print (token.text)
