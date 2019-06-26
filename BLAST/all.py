import string
import re
from itertools import combinations

sequ1=[]
sequ2=[]
seque1=[]
seque2=[]


def get_text(start_text, end, word):
    start = word.find(start_text)
    if start >= 0:
        start += len(start_text)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()

def com(list1):
    res_list = []
    #for i in range (len (list1) + 1):
    res_list += list (combinations (list1, 2))
    return res_list


def matrix(seq1,seq2,n1,n2):
    n = len(seq2)
    m = len(seq1)
    g = -3
    match = 2
    dismatch = -1
    #print seq1
    #print seq2
    print "this program will alignment the insulin sequences of ", n1, " and ", n2, "\n"
    matrix = []
    for i in range(0, m+1):
        T=[]
        for j in range(0, n+1):
            T.append (0)
        matrix.append(T)
    for sii in range(0, m+1):
            matrix[sii][0] = sii*g
    for sjj in range(0, n+1):
            matrix[0][sjj] = sjj*g
    for siii in range(1, m+1):
        for sjjj in range(1, n+1):
            if seq1[siii-1]==seq2[sjjj-1]:
                q=match
            else:
                q=dismatch
            matrix[siii][sjjj] = max(matrix[siii-1][sjjj] + g, matrix[siii - 1][sjjj - 1] + q, matrix[siii][sjjj-1] + g)
        sequ1 = [seq1[m-1]]
        sequ2 = [seq2[n-1]]
    #print sequ1
    #print sequ2
    while m > 0 and n > 0:
        if max(matrix[m][n-1], matrix[m-1][n-1], matrix[m-1][n]) == matrix[m-1][n-1]:
            m -= 1
            n -= 1
            sequ1.append(seq1[m-1])
            sequ2.append(seq2[n-1])
        elif max(matrix[m][n-1], matrix[m-1][n-1], matrix[m-1][n]) == matrix[m][n-1]:
            n -= 1
            sequ1.append('-')
            sequ2.append(seq2[n-1])
        elif max(matrix[m][n-1], matrix[m-1][n-1], matrix[m-1][n]) == matrix[m-1][n]:
            m -= 1
            sequ1.append(seq1[m-1])
            sequ2.append('-')
    #print sequ1
    #print sequ2
    sequ1.reverse()
    sequ2.reverse()
    seque1 = string.join(sequ1, '')
    seque2 = string.join(sequ2, '')
    global score
    score = 0
    for k in range(0, len(seque1)):
        if seque1[k] == seque2[k]:
           score += 1
    score = float(score)/len(seque2)
    print seque1
    print seque2
    print "\n","the score of the ",n1," and ",n2," is ",score,"\n"



fa = open("./alignment-sequence-test.fasta")
fasta=fa.read()
#print fasta

s=re.split('>',fasta)
#print s

del s[0]

for q in range(0,len(s)):
    s[q]=re.sub(r'\s+','',s[q])
#print s

name=s[:]
sequences=s[:]

for q in range(0,len(s)):
    name[q] = get_text("[","]",name[q])
    sequences[q] += ":"
    sequences[q] = get_text("]",":",sequences[q])

#print name
#print sequences

coname=com(name)
coseq=com(sequences)

#print coname
#print sequences

for x in range(0,len(coname)):
    n1=coname[x][0]
    #print n1
    n2=coname[x][1]
    #print n2
    seq1=coseq[x][0]
    seq2=coseq[x][1]
    matrix(seq1,seq2,n1,n2)
    #alignment(seq2,seq1,n2,n1)

fa.close()

