import spacy

print "import spacy"

nlp = spacy.load("en")

print "load en"

doc = unicode(open("input-small.txt").read().decode("utf-8"))

print "open txt"

doc = nlp(document)


