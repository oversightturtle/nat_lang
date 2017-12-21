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

class parts_of_speech:
  instances = []
  total_counter = 0
  total_change_counter = 0
  def __init__(self, name):
    self.counter = 0
    self.change_counter = 0
    self.name = name
    parts_of_speech.instances.append(self)
  def inc_count(self):
    self.counter += 1
    parts_of_speech.total_counter += 1
  def inc_change(self):
    self.change_counter += 1
    parts_of_speech.total_change_counter += 1
  def get_counter(self):
    return self.counter
  def get_change(self):
    return self.change_counter
  def get_name(self):
    return self.name
  def get_total_counter(self):
    return parts_of_speech.total_counter
  def get_total_counter(self):
    return parts_of_speech.total_change_counter

noun = parts_of_speech("NOUN")
verb = parts_of_speech("VERB")
adj = parts_of_speech("ADJ")
adv = parts_of_speech("ADV")
cconj = parts_of_speech("CCONJ")
adp = parts_of_speech("ADP")
det = parts_of_speech("DET")
pron = parts_of_speech("PRON")
propn = parts_of_speech("PROPN")

for token in doc:
  for ins in parts_of_speech.instances:
    if token.pos_ == ins.name:
      ins.inc_count()
      if token.ent_type_ == '':
       ins.inc_change()

for ins in parts_of_speech.instances:
  print "#", ins.get_name() , ins.get_counter() ,
  print "\t#c_", ins.get_name(), ins.get_change(),
  print "\t#%u", str(float(ins.get_counter)/float(ins.get_total_counter))[:4],
  print "\t#%c", str(float(ins.get_change())/float(ins.get_counter()))[:4]


