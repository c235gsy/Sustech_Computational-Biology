import re
import string
import json
import os
import copy
import string
import re
import time

start=time.clock()
def get_text(start_text, end, word):
    start = word.find(start_text)
    if start >= 0:
        start += len(start_text)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()

def get_word(i,seq):
    word = seq[i-1:i+7]
    return word

def matrix(seq1,seq2,n1,n2):
    n = len(seq2)
    m = len(seq1)
    g = -3
    match = 2
    dismatch = -2
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
    seque1 = seque1[20:-20]
    seque2 = seque2[20:-20]
    global score
    score = 0
    for k in range(0, len(seque1)):
        if seque1[k] == seque2[k]:
           score += 1
    score = float(score)/len(seque2)
    print seque1
    print seque2
    print "\n","the score of the ",n1," and ",n2," is ",score,"\n"




fa = open("./lambda_virus.fa")
#fa = open("./alignment-sequence.fasta")
lab=fa.read()
#print lab

name1 = get_text("| ","\n",lab)
lab += ":"
sequences1 = get_text("\n",":",lab)


sequences1=re.sub(r'\s+','',sequences1)

print name1
#print sequences1

Dictionary = {}

for i in range(1,(len(sequences1)-7)):
    Dictionary[i] = get_word(i,sequences1)
#for i in range(1,(len(sequences1)-10),5):
    #print i,Dictionary[i]

# all right below

file = open("./Dictionary1","w+")
json.dump(Dictionary,file)
file.close()


file = open("./Dictionary1","r+")
Dictionary = json.load(file)

#########################
#########################
########################
seq_dict = {}

file = open("./search1.txt")
seq = file.read()
seq=re.sub(r'\s+','',seq)
sequences2=seq
file.close

print sequences2

for i in range(1,(len(sequences2)-7)):
    seq_dict[i] = get_word(i,sequences2)
    #print i,seq_dict[i]


match_data = []
for i in range(1,(len(sequences2)-7)):
    for (key, value) in Dictionary.items():
        if value.startswith(seq_dict[i]):
            #print key
            match_data.append(key)


match_data= sorted(match_data)
copy_match_data = copy.deepcopy(match_data)
c = len(copy_match_data)-1
limit=len(sequences2)/2
print limit
for i in range(0,c):
    a=int(copy_match_data[i+1])
    b=int(copy_match_data[i])
    distance= a-b
    if distance < 0:
        distance = abs(distance)
        if distance > (22):
            match_data[i+1]=0
    if distance > 0:
        if distance > (22):
            match_data[i]=0
match_data= sorted(match_data)



p=[]
p.append(0)
for i in range(0,c):
    a = int (match_data[i + 1])
    b = int (match_data[i])
    distance = abs(a - b)
    if distance >(22):
        p.append(i + 1)
print p

seed=[]
for i in range(0,len(p)-1):
    seed.append(match_data[int(p[i]):int(p[i+1])])
print seed

seed_len=[]
for i in range(1,len(seed)):
    seed_len.append(len(seed[i]))
print seed_len

seed_l=0
seed_o=0
for i in range(0,len(seed)-1):
    if max(seed_len)==seed_len[i]:
        (seed_s) = int(seed[i+1][0])
        seed_o = int(seed[i+1][len(seed[i+1])-1])
print seed_s, seed_o

print "for file : search1.txt"
#print(match_data)

a=int(seed_s-19)
b=int(seed_o+27)
c=int(seed_s-17)
d=int(seed_o+7)

s1=sequences1[a:b]
s2=sequences1[c:seed_s]+sequences2+sequences1[d:b]
matrix(s1,s2,"lib","search1")
#########################
#########################
########################
seq_dict = {}

file = open("./search2.txt")
seq = file.read()
seq=re.sub(r'\s+','',seq)
sequences2=seq
file.close

print sequences2

for i in range(1,(len(sequences2)-7)):
    seq_dict[i] = get_word(i,sequences2)
    #print i,seq_dict[i]


match_data = []
for i in range(1,(len(sequences2)-7)):
    for (key, value) in Dictionary.items():
        if value.startswith(seq_dict[i]):
            #print key
            match_data.append(key)

match_data= sorted(match_data)
copy_match_data = copy.deepcopy(match_data)
c = len(copy_match_data)-1

for i in range(0,c):
    a=int(copy_match_data[i+1])
    b=int(copy_match_data[i])
    distance= a-b
    count=0
    if distance < 0:
        distance = abs(distance)
        if distance > (len(sequences2)/2):
            match_data[i+1]=0
            count+=1
    if distance > 0:
        if distance > (len(sequences2)/2):
            match_data[i]=0
match_data= sorted(match_data)


print "for file : search2.txt"
print(match_data)

p=[]
p.append(0)
for i in range(0,c):
    a = int (match_data[i + 1])
    b = int (match_data[i])
    distance = abs(a - b)
    if distance >(22):
        p.append(i + 1)
print p

seed=[]
for i in range(0,len(p)-1):
    seed.append(match_data[int(p[i]):int(p[i+1])])
print seed

seed_len=[]
for i in range(1,len(seed)):
    seed_len.append(len(seed[i]))
print seed_len

seed_l=0
seed_o=0
for i in range(0,len(seed)-1):
    if max(seed_len)==seed_len[i]:
        (seed_s) = int(seed[i+1][0])
        seed_o = int(seed[i+1][len(seed[i+1])-1])
print seed_s, seed_o

print "for file : search2.txt"
#print(match_data)

a=int(seed_s-19)
b=int(seed_o+27)
c=int(seed_s-19)
d=int(seed_o+7)

s1=sequences1[a:b]
s2=sequences1[c:seed_s]+sequences2+sequences1[d:b]
matrix(s1,s2,"lib","search2")


end = time.clock()
print end - start

'''
seq = "ATGAAAATTTTCCGGTTTAAGGCGTTTCCGTTCTTCTTCGTCATAACTTAATGTTTTTATTTAAAATACCCT"

seq_dict = {}

sequences2=seq

for i in range(1,(len(sequences2)-10),11):
    seq_dict[i] = get_word(i,sequences2)
    print i,seq_dict[i]


match_data = []
for i in range(1,(len(sequences2)-10),11):
    for (key, value) in Dictionary.items():
        if value.startswith(seq_dict[i]):
            print key
            match_data.append(key)

print(match_data)
'''