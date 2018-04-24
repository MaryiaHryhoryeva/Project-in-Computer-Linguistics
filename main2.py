import numpy as np
import nltk
from docx import Document
from nltk import tokenize
from nltk.stem import WordNetLemmatizer
import re


import socket
import sys
import time
import random
import string

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)


import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

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

fp = open("tenses.txt")
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

#print "presentPerf:"
#print futureSimple
#print "presentPerfTags:"
#print futureSimpleTags

"""res = int(raw_input("Which tense would you like to train? \n"
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
"""
sentDots = ""

while True:
    # Wait for a connection
     print >>sys.stderr, 'waiting for a connection'
     connection, client_address = sock.accept()
     try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                res = int(connection.recv(16))
                print sys.stderr, 'received "%s"' % res

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

                if res == 2:
                    for i in range(len(presentContTags)):
                        sent = presentContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ") or (sent[idx][1] == "VBG"):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        """for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ"):
                                if sent[idx][0] == words[0]:
                                    for j in range(len(sent)):
                                        if sent[j][1] == "VBG":
                                            if sent[j][0] == words[1]:
                                                print "Correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 3:
                    for i in range(len(presentPerfTags)):
                        sent = presentPerfTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ") or (sent[idx][1] == "VBN"):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        """for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ"):
                                if sent[idx][0] == words[0]:
                                    for j in range(len(sent)):
                                        if sent[j][1] == "VBN":
                                            if sent[j][0] == words[1]:
                                                print "Correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 4:
                    for i in range(len(presentPerfContTags)):
                        sent = presentPerfContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ") or (sent[idx][1] == "VBN") or (sent[idx][1] == "VBG"):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        """for idx in range(len(sent)):
                            if (sent[idx][1] == "VBP") or (sent[idx][1] == "VBZ"):
                                if sent[idx][0] == words[0]:
                                    for i2 in range(len(sent)):
                                        if sent[i2][1] == "VBN":
                                            if sent[i2][0] == words[1]:
                                                for j in range(len(sent)):
                                                    if sent[j][1] == "VBG":
                                                        if sent[j][0] == words[2]:
                                                            print "Correct"
                                                        else:
                                                            print "Not correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 5:
                    for i in range(len(pastSimpleTags)):
                        sent = pastSimpleTags[i]
                        word = ""
                        for idx in range(len(sent)):
                            if sent[idx][1] == "VBD":
                                word = sent[idx][0]
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        word2 = lemmatizer.lemmatize(word, pos="v")
                        print "Type the word \'" + word2 + "\' in the right tense: "
                        words = raw_input()
                        for idx in range(len(sent)):
                            if sent[idx][1] == "VBD":
                                if sent[idx][0] == words:
                                    print "Correct"
                                else:
                                    print "Not correct"
                        sentDots = ""

                if res == 6:
                    for i in range(len(pastContTags)):
                        sent = pastContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent)-2 and sent[idx][1] == "VBD" and sent[idx+2][1] == "VBG") or
                                        (idx < len(sent) - 1 and sent[idx][1] == "VBD" and sent[idx + 1][1] == "VBG") or
                                                 (idx > 1 and sent[idx][1] == "VBG" and sent[idx - 2][1] == "VBD") or
                                                        (idx > 0 and sent[idx][1] == "VBG" and sent[idx - 1][1] == "VBD")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        """for idx in range(len(sent)):
                            if ((idx < len(sent)-2 and sent[idx][1] == "VBD" and sent[idx+2][1] == "VBG") or
                                        (idx < len(sent) - 1 and sent[idx][1] == "VBD" and sent[idx + 1][1] == "VBG")):
                                if sent[idx][0] == words[0]:
                                    for j in range(len(sent)):
                                        if ((j > 1 and sent[j][1] == "VBG" and sent[j - 2][1] == "VBD") or
                                                        (j > 0 and sent[j][1] == "VBG" and sent[j - 1][1] == "VBD")):
                                            if sent[j][0] == words[1]:
                                                print "Correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 7:
                    for i in range(len(pastPerfTags)):
                        sent = pastPerfTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent)-2 and sent[idx][1] == "VBD" and sent[idx+2][1] == "VBN") or
                                        (idx < len(sent) - 1 and sent[idx][1] == "VBD" and sent[idx + 1][1] == "VBN") or
                                                 (idx > 1 and sent[idx][1] == "VBN" and sent[idx - 2][1] == "VBD") or
                                                        (idx > 0 and sent[idx][1] == "VBN" and sent[idx - 1][1] == "VBD")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        """for idx in range(len(sent)):
                            if ((idx < len(sent)-2 and sent[idx][1] == "VBD" and sent[idx+2][1] == "VBN") or
                                        (idx < len(sent) - 1 and sent[idx][1] == "VBD" and sent[idx + 1][1] == "VBN")):
                                if sent[idx][0] == words[0]:
                                    for j in range(len(sent)):
                                        if ((j > 1 and sent[j][1] == "VBN" and sent[j - 2][1] == "VBD") or
                                                        (j > 0 and sent[j][1] == "VBN" and sent[j - 1][1] == "VBD")):
                                            if sent[j][0] == words[1]:
                                                print "Correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""


                if res == 8:
                    for i in range(len(pastPerfContTags)):
                        sent = pastPerfContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent) - 2 and sent[idx][1] == "VBD" and sent[idx+1][1] == "VBN" and sent[idx+2][1] == "VBG") or
                                        (idx > 2 and sent[idx][1] == "VBG" and sent[idx - 1][1] == "VBN" and sent[idx - 2][1] == "VBD") or
                                            (1< idx < len(sent)-1 and sent[idx-1][1] == "VBD" and sent[idx][1] == "VBN" and sent[idx +1][1] == "VBG")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(word)):
                            word2[idx] = lemmatizer.lemmatize(word[idx], pos="v")
                            print "Type the word \'" + word2[idx] + "\' in the right tense: "
                            words.append(raw_input())
                        if compare(word, words) == True:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 9:
                    for i in range(len(futureSimpleTags)):
                        sent = futureSimpleTags[i]
                        word = []
                        words = []
                        word2 = {}
                        pronoun = 0
                        for idx in range(len(sent)):
                            if ((idx < len(sent) - 1 and sent[idx][1] == "MD" and sent[idx + 1][1] == "VB") or
                                    (idx > 0 and sent[idx - 1][1] == "MD" and sent[idx][1] == "VB")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        for idx in range(len(sent)):
                            if (idx < len(sent) - 1 and (sent[idx][0] == "I" or sent[idx][0] == "we" or sent[idx][0] == "We") and sent[idx + 1][1] == "MD"):
                                pronoun = 1
                        word2[1] = lemmatizer.lemmatize(word[1], pos="v")
                        print "Type the word \'" + word2[1] + "\' in the right tense: "
                        words.append(raw_input())
                        """for idx in range(len(sent)):
                            if ((idx < len(sent)-2 and sent[idx][1] == "VBD" and sent[idx+2][1] == "VBG") or
                                        (idx < len(sent) - 1 and sent[idx][1] == "VBD" and sent[idx + 1][1] == "VBG")):
                                if sent[idx][0] == words[0]:
                                    for j in range(len(sent)):
                                        if ((j > 1 and sent[j][1] == "VBG" and sent[j - 2][1] == "VBD") or
                                                        (j > 0 and sent[j][1] == "VBG" and sent[j - 1][1] == "VBD")):
                                            if sent[j][0] == words[1]:
                                                print "Correct"
                                            else:
                                                print "Not correct"
                                else:
                                    print "Not correct"
                                    """
                        if pronoun == 0:
                            res = "will " + word[1]
                            if res == words[0]:
                                print "Correct"
                            else:
                                print "Not correct"
                        if pronoun == 1:
                            res = "will " + word[1]
                            res2 = "shall " + word[1]
                            if (res == words[0] or res2 == words[0]):
                                print "Correct"
                            else:
                                print "Not correct"
                        sentDots = ""

                if res == 10:
                    for i in range(len(futureContTags)):
                        sent = futureContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent) - 3 and sent[idx][1] == "MD" and sent[idx + 2][1] == "VB" and sent[idx + 3][1] == "VBG") or
                                    (idx < len(sent) - 2 and sent[idx][1] == "MD" and sent[idx + 1][1] == "VB" and sent[idx + 2][1] == "VBG") or
                                    (idx > 1 and idx < len(sent) - 1 and sent[idx - 2][1] == "MD" and sent[idx][1] == "VB" and sent[idx + 1][1] == "VBG") or
                                    (idx > 0 and idx < len(sent) - 1 and sent[idx - 1][1] == "MD" and sent[idx][1] == "VB" and sent[idx + 1][1] == "VBG") or
                                    (idx > 2 and sent[idx - 3][1] == "MD" and sent[idx - 1][1] == "VB" and sent[idx][1] == "VBG") or
                                    (idx > 1 and sent[idx - 2][1] == "MD" and sent[idx - 1][1] == "VB" and sent[idx][1] == "VBG")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        word2[2] = lemmatizer.lemmatize(word[2], pos="v")
                        res = "will be " + word[2]
                        print "Type the word \'" + word2[2] + "\' in the right tense: "
                        words.append(raw_input())
                        if res == words[0]:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 11:
                    for i in range(len(futurePerfTags)):
                        sent = futurePerfTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent) - 2 and sent[idx][1] == "MD" and sent[idx + 1][1] == "VB" and sent[idx + 2][1] == "VBN") or
                                    (idx > 0 and idx < len(sent) - 1 and sent[idx - 1][1] == "MD" and sent[idx][1] == "VB" and sent[idx + 1][1] == "VBN") or
                                    (idx > 1 and sent[idx - 2][1] == "MD" and sent[idx - 1][1] == "VB" and sent[idx][1] == "VBN")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        print sentDots
                        word2[2] = lemmatizer.lemmatize(word[2], pos="v")
                        res = "will have " + word[2]
                        print "Type the word \'" + word2[2] + "\' in the right tense: "
                        words.append(raw_input())
                        if res == words[0]:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                if res == 12:
                    for i in range(len(futurePerfContTags)):
                        sent = futurePerfContTags[i]
                        word = []
                        words = []
                        word2 = {}
                        for idx in range(len(sent)):
                            if ((idx < len(sent) - 3 and sent[idx][1] == "MD" and sent[idx + 1][1] == "VB" and sent[idx + 2][1] == "VBN" and sent[idx + 3][1] == "VBG") or
                                    (idx > 0 and idx < len(sent) - 2 and sent[idx - 1][1] == "MD" and sent[idx][1] == "VB" and sent[idx + 1][1] == "VBN" and sent[idx + 2][1] == "VBG") or
                                    (idx > 1 and idx < len(sent) - 1 and sent[idx - 2][1] == "MD" and sent[idx - 1][1] == "VB" and sent[idx][1] == "VBN" and sent[idx+1][1] == "VBG") or
                                    (idx > 2  and sent[idx - 3][1] == "MD" and sent[idx - 2][1] == "VB" and sent[idx - 1][1] == "VBN" and sent[idx][1] == "VBG")):
                                word.append(sent[idx][0])
                                sentDots += "..."
                                sentDots += " "
                            else:
                                sentDots += sent[idx][0]
                                sentDots += " "
                        #print sentDots

                        word2[3] = lemmatizer.lemmatize(word[3], pos="v")
                        res = "will have been " + word[3]
                        #print "Type the word \'" + word2[3] + "\' in the right tense: "
                        data = sentDots + "\n Type the word \'" + word2[3] + "\' in the right tense: "
                        print sys.stderr, 'sending data back to the client'
                        connection.sendall(data)
                        words.append(raw_input())
                        if res == words[0]:
                            print "Correct"
                        else:
                            print "Not correct"
                        sentDots = ""

                else:
                    print  sys.stderr, 'no more data from', client_address
                    break
     finally:
            # Clean up the connection
            connection.close()