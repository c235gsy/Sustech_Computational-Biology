import re
import json
import time
import gc

start = time.clock()

def get_text(start_text, end, word):
    start = word.find(start_text)
    if start >= 0:
        start += len(start_text)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()

def get_word(i,seq):
    word = seq[i-1:i+10]
    return word

def dealWithseq(lab):
    lab += ":"
    seq = get_text("\n",":",lab)
    seq = re.sub(r'\s+'|"'",'',seq)
    return seq

def buildLibrary(seq,chromName,counter):
    subDic = {}
    for i in range (1, (len (seq) - 9)):
        word = get_word (i, seq)
        subDic[word] = ""

    for i in range (1, (len (seq) - 9)):
        word = get_word (i, seq)
        subDic[word] += ("%d" % (i+counter) + " ")

    for (key, value) in subDic.items ():
        with open ("./library/%s" % chromName+"/%s"%key, "a+") as r_file:
            r_file.write (value)

    print "finish",chromName,counter


for i in range (1,2):
    chromName = ""
    if (i < 23):
        chromName = "chr%d"%i
    if (i == 23):
        chromName = "chrX"
    if (i == 24):
        chromName = "chrY"
    if (i == 25):
        chromName = "chrMT"
    print chromName


    j = 1
    p = 1
    while p == 1:
        fa = open ("./Dictionary/%s" % chromName, "r+")
        seq = json.load (fa)
        len_s = len (seq)
        fa.close ()
        seq1 = seq[j - 1:min (j + 9999999, len_s - 9)]
        seq = ""

        buildLibrary (seq1, chromName, j-1)

        j += 9999990

        if j + 9 >= len_s - 9:
            break
    print "finish library",chromName

'''
    fa = open ("./Dictionary/%s" % chromName, "r+")
    seq = json.load (fa)
    fa.close ()
    buildLibrary(seq,chromName,0)
'''



end=time.clock()
print "time: ",end - start

gc.collect()

'''
j=1
    p=1
    while p==1:
        fa = open ("./Dictionary/%s" % chromName, "r+")
        seq = json.load (fa)
        len_s = len(seq)
        fa.close ()
        seq1 = seq[j-1:min(j+9999999,len_s-9)]
        seq = ""
        print "finidsh", j
        buildLibrary(seq1,chromName,j)

        j+=9999990

        if j+9 >= len_s-9:
            break
    print "finish library"
'''