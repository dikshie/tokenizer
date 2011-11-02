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

panjang=len(lines_3)
rem=[]
rem_2=[]
rem_3=[]
l=[]
h=[]
z=[]

for i in range(panjang):
    rem.append(lines_3[i])
    token = ntk.word_tokenize(rem[i])
    rem_2.append(token[2:])
    for j in range(len(lines_2)):
        posn=re.match(token[0],lines_2[j])
        if posn==None:
            pass
        else:
            pos_n=j
    l=rem_2[i]
    for k in range(len(l)):
        if (k % 2)==0:
            h.append(l[k])
    z.append(h) 
    h=[]

print z
#print len(rem_3)
#print rem_3
#for k in range(len(rem_2[i])):
#        l=rem_2[i]
#        if (k % 2) == 0:
#            rem_3.append(l[k])
#print rem_3

