import numpy as np
import nltk
from docx import Document
from nltk import tokenize
from nltk.stem import WordNetLemmatizer
import re

lemmatizer = WordNetLemmatizer()

sentences = []
tagSent = [] #sentences made of tags
taggedWords = [] #words with tags



presentSimple = []
presentCont = []
presentPerf = []
presentPerfCont = []
pastSimple = []
pastCont = []
pastPerf = []
pastPerfCont = []
futureSimple = []
futureCont = []
futurePerf = []
futurePerfCont = []

presentSimpleTags = []
presentContTags = []
presentPerfTags = []
presentPerfContTags = []
pastSimpleTags = []
pastContTags = []
pastPerfTags = []
pastPerfContTags = []
futureSimpleTags = []
futureContTags = []
futurePerfTags = []
futurePerfContTags = []

from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
english_postagger = POS_Tag('C:\Users\ASUS\Desktop\stanford-postagger-full-2014-08-27\stanford-postagger-full-2014-08-27\models\english-bidirectional-distsim.tagger', 'C:\Users\ASUS\Desktop\stanford-postagger-full-2014-08-27\stanford-postagger-full-2014-08-27\stanford-postagger.jar')

fp = open("test.txt")
data = fp.read()
for sent in tokenize.sent_tokenize(data):
    sentences.append(sent)
for sent in sentences:
    text = nltk.word_tokenize(sent)
    tags = english_postagger.tag(text)
    #print tags
    taggedWords.append(tags)
    """text = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(text)
    print tags"""

    t = ""
    for i in range(len(tags)):
        t = t + tags[i][1] + " "

    tagSent.append(t)
print tagSent
for idx, tag in enumerate(tagSent):
    #PRESENT
    if (re.match(r'^(\w|[,$\s]){0,50}(VBP|VBZ) (?!(VBG|VBN))(\w|[,;$\s]){0,50} (?!(VBN|VBG))(\w|[,;$\s]){0,50}(\s?). $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBG|VBN)(\w|[,$\s]){0,50} . $', tag) is None):
        presentSimple.append(sentences[idx])
        presentSimpleTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBP|VBZ) (?!(VBN))(\w|[,;$\s]){0,50}VBG(\w|[,;$\s]){0,50} . $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBN)(\w|[,$\s]){0,50} . $', tag) is None):
        presentCont.append(sentences[idx])
        presentContTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBP|VBZ)(\w|[,;$\s]){0,50}VBN (?!(VBG))(\w|[,;$\s]){0,50}(\s?). $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBG)(\w|[,$\s]){0,50} . $', tag) is None):
        presentPerf.append(sentences[idx])
        presentPerfTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBP|VBZ)(\w|[,;$\s]){0,50}VBN VBG(\w|[,;$\s]){0,50}(\s?). $', tag) is not None):
        presentPerfCont.append(sentences[idx])
        presentPerfContTags.append(taggedWords[idx])
    #PAST
    if (re.match(r'^(\w|[,$\s]){0,50}VBD (?!(VBG|VBN))(\w|[,;$\s]){0,50} (?!(VBG|VBN))(\w|[,;$\s]){0,50}(\s?). $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBG|VBN)(\w|[,$\s]){0,50} . $', tag) is None):
        pastSimple.append(sentences[idx])
        pastSimpleTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBD) (?!(VBN))(\w|[,;$\s]){0,50}VBG(\w|[,;$\s]){0,50} . $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBN)(\w|[,$\s]){0,50} . $', tag) is None):
        pastCont.append(sentences[idx])
        pastContTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBD) (?!(VBG))(\w|[,;$\s]){0,50}(VBN) (?!(VBG))(\w|[,;$\s]){0,50}(\s?). $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBG)(\w|[,$\s]){0,50} . $', tag) is None):
        pastPerf.append(sentences[idx]) #either not all sentenses or excess sentenses from other tenses
        pastPerfTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(VBD)(\w|[,;$\s]){0,50}VBN VBG(\w|[,;$\s]){0,50}(\s?). $', tag) is not None):
        pastPerfCont.append(sentences[idx])
        pastPerfContTags.append(taggedWords[idx])
    #FUTURE
    if (re.match(r'^(\w|[,$\s]){0,50}(MD) (?!(VBN))(\w|[,;$\s]){0,50}VB(\w|[,;$\s]){0,50} . $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBN|VBG)(\w|[,$\s]){0,50} . $', tag) is None):
        futureSimple.append(sentences[idx])
        futureSimpleTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(MD) (?!(VBN))(\w|[,;$\s]){0,50}VB VBG(\w|[,;$\s]){0,50} . $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBN)(\w|[,$\s]){0,50} . $', tag) is None):
        futureCont.append(sentences[idx])
        futureContTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(MD)(\w|[,;$\s]){0,50}VB VBN(\w|[,;$\s]){0,50} . $', tag) is not None) and \
            (re.match(r'^(\w|[,$\s]){0,50}(VBG)(\w|[,$\s]){0,50} . $', tag) is None):
        futurePerf.append(sentences[idx])
        futurePerfTags.append(taggedWords[idx])
    if (re.match(r'^(\w|[,$\s]){0,50}(MD)(\w|[,;$\s]){0,50}VB VBN(\w|[,;$\s]){0,50} VBG(\w|[,;$\s]){0,50} . $', tag) is not None):
        futurePerfCont.append(sentences[idx])
        futurePerfContTags.append(taggedWords[idx])

print "presentSimple:"
print presentSimple
print "presentSimpleTags:"
print presentSimpleTags

res = int(raw_input("Which tense would you like to train? \n"
      "1 - Present Simple \n"
      "2 - Present Continuous \n"
      "3 - Present Perfect \n"
      "4 - Present Perfect Continuous \n"
      "5 - Past Simple \n"
      "6 - Past Continuous \n"
      "7 - Past Perfect \n"
      "8 - Past Perfect Continuous \n"
      "9 - Future Simple \n"
      "10 - Future Continuous \n"
      "11 - Future Perfect \n"
      "12 - Future Perfect Continuous \n"
      "Your choise: "))

sentDots = ""
if res == 1:
    for i in range(len(presentSimpleTags)):
        sent = presentSimpleTags[i]
        word = ""
        for idx in range(len(sent)):
            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ"):
                word = sent[idx][0]
                sentDots += "..."
                sentDots += " "
            else:
                sentDots += sent[idx][0]
                sentDots += " "
        print sentDots
        word2 = lemmatizer.lemmatize(word, pos="v")
        print "Type the word \'" + word2 +"\' in the right tense: "
        words = raw_input()
        for idx in range(len(sent)):
            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ"):
                if sent[idx][0] == words:
                    print "Correct"
                else:
                    print "Not correct"
        sentDots = ""