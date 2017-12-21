verbose = True

def v_p(txt):
    if verbose == True:
        print txt

v_p("_INIT >> IMPORT SPACY")

import spacy

v_p("FINSH IMPORT // LOADING EN")

nlp = spacy.load("en")

v_p("LOADED EN // START TXT IMPORT")

doc = unicode(open("input-small.txt").read().decode("utf-8"))

v_p("LOADED FILE // STARTING NLP")

doc = nlp(doc)

v_p("NLP DONE ... ")

n_noun = 0
n_c_noun = 0
n_verb = 0
n_adj = 0
n_adv = 0
n_cconj = 0
n_adp = 0
n_det = 0
n_pron = 0
n_propn = 0

n_totes = 0

for token in doc:
  if token.pos_ == "NOUN":
    n_noun += 1
    n_totes += 1
    if token.ent_type_ == "":
      n_c_noun += 1
  if token.pos_ == "VERB":
    n_verb += 1
    n_totes += 1
  if token.pos_ == "ADJ":
    n_adj += 1
    n_totes += 1
  if token.pos_ == "ADV":
    n_adv += 1
    n_totes += 1
  if token.pos_ == "CCONJ":
    n_cconj += 1
    n_totes += 1  
  if token.pos_ == "ADP":
    n_adp += 1
    n_totes += 1
  if token.pos_ == "DET":
    n_det += 1
    n_totes += 1
  if token.pos_ == "PRON":
    n_pron += 1
    n_totes += 1
  if token.pos_ == "PROPN":
    n_propn += 1
    n_totes += 1
  if token.ent_type_ != "":
    print token, token.pos_
#  print token.ent_type_


print "# nouns : ", n_noun, "# c nouns", n_c_noun, "\t % c nouns:", float(n_c_noun) / float(n_totes)
print n_verb, n_adj, n_adv





