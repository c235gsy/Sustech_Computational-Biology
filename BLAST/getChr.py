import json
import re
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


x = open("./hg19.fa")
seq = x.read()
x.close()
print "read over"
seq = seq.upper()
seq = seq+"99"
seq = re.sub (r'\s+', '', seq)
print "get seq"
print len(seq)


for i in range(1,22):
    chr = get_text(">CHR%d"%i,">",seq)
    #chr = re.sub ('N', '', chr)
    print "get ",i
    file = open ("./Dictionary/chr%d"%i, "w+")
    json.dump (chr, file)
    file.close ()
    print "finish%d"%i, len(chr)

chr = get_text(">CHR22",">",seq)
#chr = re.sub ('N', '', chr)
file = open ("./Dictionary/chr22","w+")
json.dump (chr, file)
file.close ()
print "finish chr22",len(chr)

chr = get_text(">CHRX",">",seq)
#chr = re.sub ('N', '', chr)
file = open ("./Dictionary/chrX","w+")
json.dump (chr, file)
file.close ()
print "finish chrX",len(chr)

chr = get_text(">CHRY","99",seq)
#chr = re.sub ('N', '', chr)
print "get chrY"
file = open ("./Dictionary/chrY","w+")
json.dump (chr, file)
file.close ()
print "finish chrY",len(chr)


chr = get_text(">CHRM",">",seq)
#chr = re.sub ('N', '', chr)
print "get chrMT"
file = open ("./Dictionary/chrMT","w+")
json.dump (chr, file)
file.close ()
print "finish chrMT",len(chr)


end = time.clock()
print end -start


gc.collect()