import re


seq = ""
x = open("./hg19.fa")
seq = x.read()
x.close()
print "read over"
seq = seq.upper()
seq = seq+"99 "
seq = re.sub (r'\s+', '', seq)
print "get seq"
print len(seq)



for i in range (1,26):

    chromName = ""
    if (i < 23):
        chromName = "CHR%d"%i
    if (i == 23):
        chromName = "CHRX"
    if (i == 24):
        chromName = "CHRY"
    if (i== 25):
        chromName = "CHRM"

    location = seq.find(chromName)
    print location,chromName