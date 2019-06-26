import json
import time
import gc
import os
# coding: UTF-8

start=time.time()

def get_word(i,seq):
    word = seq[i-1:i+10]
    return word

for i in range (1,26):

    chromName = ""
    if (i < 23):
        chromName = "chr%d"%i
    if (i == 23):
        chromName = "chrX"
    if (i == 24):
        chromName = "chrY"
    if (i== 25):
        chromName = "chrMT"

    os.mkdir("./library/%s"%chromName)
    print "finish %s"%chromName

print time.time() - start

gc.collect()
