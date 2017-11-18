import numpy as np
import nltk
from docx import Document
from nltk import tokenize
from nltk.stem import WordNetLemmatizer
import re

lemmatizer = WordNetLemmatizer()

sentences = []
tagSent = [] #sentences made of tags

####HOW TO REMOVE FALSE SENTENSES FROM PRESENT SIMPLE AND ADD THEM TO PAST SIMPLE???
#### Do I need to use questions?

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

presentSimpleEx = []
presentContEx = []
presentPerfEx = []
presentPerfContEx = []
pastSimpleEx = []
pastContEx = []
pastPerfEx = []
pastPerfContEx = []
futureSimpleEx = []
futureContEx = []
futurePerfEx = []
futurePerfContEx = []

presentSimpleVerbs = []
presentContVerbs = []
presentPerfVerbs = []
presentPerfContVerbs = []
pastSimpleVerbs = []
pastContVerbs = []
pastPerfVerbs = []
pastPerfContVerbs = []
futureSimpleVerbs = []
futureContVerbs = []
futurePerfVerbs = []
futurePerfContVerbs = []


from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
english_postagger = POS_Tag('C:\Users\ASUS\Desktop\stanford-postagger-full-2014-08-27\stanford-postagger-full-2014-08-27\models\english-bidirectional-distsim.tagger', 'C:\Users\ASUS\Desktop\stanford-postagger-full-2014-08-27\stanford-postagger-full-2014-08-27\stanford-postagger.jar')

fp = open("tenses.txt")
data = fp.read()
for sent in tokenize.sent_tokenize(data):
    sentences.append(sent)
for sent in sentences:
    text = nltk.word_tokenize(sent)
    tags = english_postagger.tag(text)
    print tags

    """text = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(text)
    print tags"""

    t = ""
    for i in range(len(tags)):
        t = t + tags[i][1] + " "
    tagSent.append(t)
print tagSent
for idx, tag in enumerate(tagSent):
    if (re.match(r'^(\w|[,\s]){0,50}(VBP|VBZ)(\w|[,;\s]){0,50} (?!(VBN|VBG))(\w|[,;\s]){0,50} . $', tag) is not None) \
            and (re.search(r'(VBN|VBG)', tag) is None):
        presentSimple.append(sentences[idx])

print presentSimple
