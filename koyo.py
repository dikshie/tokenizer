import sys
import string
import re
import numpy
import nltk.tokenize as ntk

lemma=open('lemma.txt','r')
lines_1 = lemma.readlines()
lemma.close()
kolom=len(lines_1)
#print type(lines_1)

entry=open('entry.txt','r')
lines_2 = entry.readlines()
entry.close()
baris=len(lines_2)
#print type(lines_2)

M=numpy.zeros((baris,kolom),int)

padanan=open('padanan.txt','r')
lines_3 = padanan.readlines()
padanan.close()

#print lines_3
#print type(lines_3)
#print len(lines_3)

rem=[]
for i in range(len(lines_3)):
    rem.append(lines_3[i])
#    print i, lines_3[i]
    token = ntk.word_tokenize(rem[i])
#    print token[0]
    for j in range(len(lines_2)):
        posn=re.match(token[0],lines_2[j])
        if posn==None:
            pass
        else:
            print j


#token=ntk.word_tokenize(lines_3[0])
#print lines_3[0]
#print token
