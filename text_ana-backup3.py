verbose = True

def v_p(txt):
    if verbose == True:
        print txt

v_p("_INIT >> IMPORT SPACY")

import spacy

v_p("FINSH IMPORT // LOADING EN")

nlp = spacy.load("en")

v_p("LOADED EN // START TXT IMPORT")

doc = unicode(open("input-custom.txt").read().decode("utf-8"))

v_p("LOADED FILE // STARTING NLP")

doc = nlp(doc)

v_p("NLP DONE ... ")

class parts_of_speech:
  instances = []
  total_counter = 0
  total_change = 0
  def __init__(self, name, s_c):
    self.counter = 0
    self.change = 0
    self.name = name  # name to compare (formal too)
    self.s_c = s_c    # should this be changed
    parts_of_speech.instances.append(self)
  def inc_count(self):
    self.counter += 1
    parts_of_speech.total_counter += 1
  def inc_change(self):
    self.change += 1
    parts_of_speech.total_change += 1

####### AFF A T/F FOR COUNTING THE POS THAT WE CAN CHANGE
####### ADD A TOTAL COLL

noun = parts_of_speech("NOUN", True)
verb = parts_of_speech("VERB", True)
adj = parts_of_speech("ADJ", True)
adv = parts_of_speech("ADV", True)
cconj = parts_of_speech("CCONJ", False)
adp = parts_of_speech("ADP", False)
det = parts_of_speech("DET", False)
pron = parts_of_speech("PRON", False)
propn = parts_of_speech("PROPN", False)
#ins = parts_of_speech("IGNORE", False)

for token in doc:
  for ins in parts_of_speech.instances:
    if token.pos_ == ins.name:
      ins.inc_count()
      if token.ent_type_ == '':
       ins.inc_change()

for ins in parts_of_speech.instances:
  print "#", ins.name , ins.counter ,
  print "\t#c_", ins.name, ins.change,
  print "\t#%u", str(float(ins.counter)/float(ins.total_counter))[:4],
  print "\t#%c", str(float(ins.change)/float(ins.counter))[:4],
  print "\tBC",ins.s_c

tot_workingdef = 0
for ins in parts_of_speech.instances:
  global tot_workingdef
  if ins.s_c == True:
    tot_workingdef += ins.change
print "TOTALCHANGE : ", tot_workingdef, 
print "FLOAT : ", str(float(tot_workingdef) / float(parts_of_speech.total_counter))[:4]




