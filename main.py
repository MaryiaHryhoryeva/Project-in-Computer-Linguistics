import numpy as np
import nltk
from docx import Document
from nltk import tokenize
from nltk.stem import WordNetLemmatizer


"""document = Document()
document.save('To-Kill-a-Mockingbird.docx')
text=nltk.word_tokenize("	He had been watching her for some time when she turned and smiled.")
print nltk.pos_tag(text)"""

"""tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()
print '\n-----\n'.join(tokenizer.tokenize(data))"""

lemmatizer = WordNetLemmatizer()

sentences = []

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

fp = open("test.txt")
data = fp.read()
for sent in tokenize.sent_tokenize(data):
    sentences.append(sent)
for sent in sentences:
    text = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(text)
    print tags
    for i in range(len(tags)):
        if tags[i][1] == 'VBP':
            i = i + 1
            if tags[i][1] == 'VBN':
                i = i + 1
                if tags[i][1] == 'VBG':
                    if sent not in presentPerfCont:
                        presentPerfCont.append(sent)
                        presentPerfContVerbs.append(tags[i][0])
                        sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0] + " " + tags[i][0], "...")
                        presentPerfContEx.append(sentNew)
                        continue
                else:
                    if sent not in presentPerf:
                        presentPerf.append(sent)
                        presentPerfVerbs.append(tags[i - 1][0])
                        sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0], "...")
                        presentPerfEx.append(sentNew)
                        continue
            if tags[i][1] == 'VBG':
                if sent not in presentCont:
                    presentCont.append(sent)
                    presentContVerbs.append(tags[i][0])
                    sentNew = sent.replace(tags[i-1][0] + " " + tags[i][0], "...")
                    presentContEx.append(sentNew)
                    continue
            else:
                if sent not in presentSimple:
                    presentSimple.append(sent)
                    presentSimpleVerbs.append(tags[i-1][0])
                    sentNew = sent.replace(tags[i-1][0], "...")
                    presentSimpleEx.append(sentNew)
                    continue

    for i in range(len(tags)):
        if tags[i][1] == 'VBD':
            i = i + 1
            if tags[i][1] == 'VBN':
                i = i + 1
                if tags[i][1] == 'VBG':
                    if sent not in pastPerfCont:
                        pastPerfCont.append(sent)
                        pastPerfContVerbs.append(tags[i][0])
                        sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0] + " " + tags[i][0], "...")
                        pastPerfContEx.append(sentNew)
                        continue
                else:
                    if sent not in pastPerf:
                        pastPerf.append(sent)
                        pastPerfVerbs.append(tags[i - 1][0])
                        sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0], "...")
                        pastPerfEx.append(sentNew)
                        continue
            if tags[i][1] == 'VBG':
                if sent not in pastCont:
                    pastCont.append(sent)
                    pastContVerbs.append(tags[i][0])
                    sentNew = sent.replace(tags[i - 1][0] + " " + tags[i][0], "...")
                    pastContEx.append(sentNew)
                    continue
            else:
                if sent not in pastSimple:
                    pastSimple.append(sent)
                    pastSimpleVerbs.append(tags[i - 1][0])
                    sentNew = sent.replace(tags[i - 1][0], "...")
                    pastSimpleEx.append(sentNew)
                    continue

    for i in range(len(tags)):
        if (tags[i][1] == 'MD') and (tags[i + 1][1] == 'VB'):
            i = i + 2
            if tags[i][1] == 'VBN':
                i = i + 1
                if tags[i][1] == 'VBG':
                    if sent not in futurePerfCont:
                        futurePerfCont.append(sent)
                        futurePerfContVerbs.append(tags[i][0])
                        sentNew = sent.replace(tags[i - 3][0] + " " + tags[i - 2][0] + " " + tags[i - 1][0] + " " + tags[i][0], "...")
                        futurePerfContEx.append(sentNew)
                        continue
                else:
                    if sent not in futurePerf:
                        futurePerf.append(sent)
                        futurePerfVerbs.append(tags[i - 1][0])
                        sentNew = sent.replace(tags[i - 3][0] + " " + tags[i - 2][0] + " " + tags[i - 1][0], "...")
                        futurePerfEx.append(sentNew)
                        continue
            if tags[i][1] == 'VBG':
                if sent not in futureCont:
                    futureCont.append(sent)
                    futureContVerbs.append(tags[i][0])
                    sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0] + " " + tags[i][0], "...")
                    futureContEx.append(sentNew)
                    continue
            else:
                if sent not in futureSimple:
                    futureSimple.append(sent)
                    futureSimpleVerbs.append(tags[i - 1][0])
                    sentNew = sent.replace(tags[i - 2][0] + " " + tags[i - 1][0], "...")
                    futureSimpleEx.append(sentNew)
                    continue

print "Present Simple: ", presentSimple
"""print "Present Simple: ", presentSimple
print "Present Continuous: ", presentContinuous
print "Present Perfect: ", presentPerfect
print "Present Perfect Continuous: ", presentPerfectContinuous
print "Past Simple: ", pastSimple
print "Past Continuous: ", pastContinuous
print "Past Perfect: ", pastPerfect
print "Past Perfect Continuous: ", pastPerfectContinuous
print "Future Simple: ", futureSimple
print "Future Continuous: ", futureContinuous
print "Future Perfect: ", futurePerfect
print "Future Perfect Continuous: ", futurePerfectContinuous"""


for i in range(len(presentSimpleVerbs)):
    presentSimpleVerbs[i] = lemmatizer.lemmatize(presentSimpleVerbs[i],'v')

for i in range(len(presentContVerbs)):
    presentContVerbs[i] = lemmatizer.lemmatize(presentContVerbs[i], 'v')

for i in range(len(presentPerfVerbs)):
    presentPerfVerbs[i] = lemmatizer.lemmatize(presentPerfVerbs[i], 'v')

for i in range(len(presentPerfContVerbs)):
    presentPerfContVerbs[i] = lemmatizer.lemmatize(presentPerfContVerbs[i], 'v')

####################

for i in range(len(pastSimpleVerbs)):
    pastSimpleVerbs[i] = lemmatizer.lemmatize(pastSimpleVerbs[i],'v')

for i in range(len(pastContVerbs)):
    pastContVerbs[i] = lemmatizer.lemmatize(pastContVerbs[i], 'v')

for i in range(len(pastPerfVerbs)):
    pastPerfVerbs[i] = lemmatizer.lemmatize(pastPerfVerbs[i], 'v')

for i in range(len(pastPerfContVerbs)):
    pastPerfContVerbs[i] = lemmatizer.lemmatize(pastPerfContVerbs[i], 'v')

#####################

for i in range(len(futureSimpleVerbs)):
    futureSimpleVerbs[i] = lemmatizer.lemmatize(futureSimpleVerbs[i],'v')

for i in range(len(futureContVerbs)):

    futureContVerbs[i] = lemmatizer.lemmatize(futureContVerbs[i], 'v')

for i in range(len(pastPerfVerbs)):
    pastPerfVerbs[i] = lemmatizer.lemmatize(pastPerfVerbs[i], 'v')

for i in range(len(pastPerfContVerbs)):
    pastPerfContVerbs[i] = lemmatizer.lemmatize(pastPerfContVerbs[i], 'v')

"""print pastSimpleVerbs
print pastContVerbs
print pastPerfVerbs
print pastPerfContVerbs"""

#print lemmatizer.lemmatize("running")
#print lemmatizer.lemmatize("running",'v')