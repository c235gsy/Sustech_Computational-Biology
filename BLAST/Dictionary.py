import re
import string
import json
import os
import time

start = time.clock()

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

fa = open("./lambda_virus.fa","r+")
#fa = open("./alignment-sequence.fasta")
lab=fa.read()
#print lab

name1 = get_text("| ","\n",lab)
lab += ":"
sequences1 = get_text("\n",":",lab)

sequences1=re.sub(r'\s+','',sequences1)

#print name1
#print sequences1
Dictionary = {}

for i in range(1,(len(sequences1)-7)):
    Dictionary[i].append(get_word (i, sequences1))
#for i in range(1,(len(sequences1)-10),5):
    print i,Dictionary[i]

# all right below

file = open("./Dictionary","w+")
json.dump(Dictionary,file)
file.close()

file = open("./Dictionary","r+")
Dictionary = json.load(file)

print Dictionary


file = open("./search1.txt")
seq = file.read()
seq=re.sub(r'\s+','',seq)
sequences2=seq
file.close

match_data = []
for i in range(1,(len(sequences2)-7)):
    for (key, value) in Dictionary.items():
        if key.startswith(get_word(i,sequences2)):
            match_data.append(value)

print "for file : search1.txt"
print match_data


file = open("./search1.txt")
seq = file.read()
seq=re.sub(r'\s+','',seq)
sequences2=seq
file.close

match_data = []
for i in range(1,(len(sequences2)-7)):
    for (key, value) in Dictionary.items():
        if key.startswith(get_word(i,sequences2)):
            match_data.append(value)

print "for file : search2.txt"
print match_data


end=time.clock()

print "time: "+ (end - start)