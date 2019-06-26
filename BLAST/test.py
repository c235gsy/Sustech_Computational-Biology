# '''data = {
#     1: "116",
#     2: "117",
#     3: "211",
#     4: "222",
#     5: "4211"
# }
#
# match_data = {}
#
# for (key, value) in data.items():
#     if value.startswith('11'):
#         match_data[key] = value
#
# print(match_data)
# import json
# import re
#
# def get_text(start_text, end, word):
#     start = word.find(start_text)
#     if start >= 0:
#         start += len(start_text)
#         end = word.find(end, start)
#         if end >= 0:
#             return word[start:end].strip()
#
# seq=open("./hg19.fa").read()
# seq.upper
#
# for i in range(1,22):
#     chr = get_text("chr%d"%i,"chr%d"%i+1,seq)
#     #chr = re.sub ('N', '', chr)
#     #chr = re.sub (r'\s+', '', chr)
#     file = open ("./Dictionary/chr%d"%i, "r+")
#     json.dump (chr, file)
#     file.close ()'''
# '''
# s="tagagatgtcccgttcgaacgctgttttacagaGGCGTGTGGACGGTGTGCCCCCTTGCTGAAGCCTCCAGCCAGCCTGAGGAAGGAGAAGTCCAGCTGTCCCCTCAACTCGCTCGACTGGAGCCTCTGAACACGGGGGCCAGTTTATGGGTTCTTCTTCACAAGAATGAAGAAGTAGGTGTTCCTTCTGACAAATTACACAAGAACATTGGCCCAAACTCTCCAAAAATGTCCATGGTCCCCAATGGATGCCTGACCCAGCATCACGTCCTTCTCCCAACCCAGTTTCAAAGTGGCCGTGAAAGGGTTTCCCACAAGATATCTGTGTACATGGCTGTCTTGCTGTCATTGTTTTATCCAGGACGTTCTCTACCATTCAGGATCTGTAAGTGTGCCCTGGAAATAGCACAGGGCTGAGAGCTGTGGTCTTGCGTGGCTCAGCCTGCCCCAGCCTCCTGTGAGGAACAGCCTGAGCAGTGTGGTTGGCCCTCACTTCCTCATCGGCTTCACCACCCCTGGCTGTGGTCTCTGCTGAAGGATCTGACACAGGCTTGCTCTGTGAAGCACAGAGCTTGCCCAGGCCCAAGGAAGGCACAACTGTGCTCTGTGCCCCTTCCTCGCTCAGATGTTGGAGGGACCATTCCTGTAAGTGCTGACCACTTCCCCAGAGTGGCAGCCTGAGCTCTGGATTAACCCTTCAGTGTCCATAGAAAACGCTCTAGCCTGCTCCTGCAGGGGTTAAAAATAGTTTGAAATCCACTCATGCAATGACCGTACACCTGTGCTTAGGGCACTGCGTTCAGCAGGAGGGCCCAGCCGGGCCTGCCCTCTGCACACTGCAGCTTCCTGGGATGGCAAGTGTGGGGCCGTGGGTCCACCCTGTTCCCAGGTCTTGGAAGCAGGCTGAGAGAGAGGATCTGCCACAGGGAGGAAAAGGGCTTTCAAGCGCTCTGGGGCCCCAGGATGGTATTCTTTGCCCAGGCTCCCCAGGAGCTCGTGGATACAACCTCACCAGCTTCCCACAGATTCCTACAATTGctgggtctgaatcttggctccaccatttaacagtggtttgactttggataaattcctaagcctttctgtgaaaggggtgaccgtagtccctactttgcagggttgttctgggTGTTTTTCCCTGACCTTCACACTTCCTGATCACCCTGGCTTACCTGTCCTGACCCCTCAGTTTTAATCTTATCCCATTAGACTGGACAGCCACCAGATCCAATCATGTGTGACTCCCACATTCACCCACCCCCTGCAGCTACATTCCACAGGAAGACCCTTCGCTAAGTAATGAGAAATGCATTATTGAGTGAGTGGAACACCTGAAAAGTTCCATGGTCTGTAGCCTACATATGACCATGTGGATTGCTAGACTAGACCTCTGATTTCAGCGGGACGATAATATTTCAGAGTAGCAGGCTAagacaaggtgggcatgtcagccataaacagcagaaggaacacaccgataatcagaatgccttggtccacagagatttttggcagtggtgaattgctcacagtgttccttagaatgaagagatggacagtcgctagagtagtctttaatccacacaacaggaaaacctctaggtctggtcaccgaagtacctaacttgaatcaccacagtggagatcatgggctctctccgagtttccagacctaagttgggtcagacctagagcatcttgattgaagggagaagccaaggccccttgagaaagaatctgtgctagtgagaaagaataccataaaccctcttccacaccttttctgaagtgtcctgcagccatCAACTAATGAAAAGGAAGTAACCTAGATGTCTCAGGGATTGCCTCAATTGACATAAATTCCTGGGAACCAAAAATGGCACTGTGGCTCACCAGTCAAAGCAGAAACTTGTGATGGTCAGTTCTTCACTTGATAGAGGTTCTAACATGAGACCGACTCACAGGGGGCCCAGTTGGTACACTATTCTCCCTATAGTTAGTTTTTCAGTTCCTGGTTGTATAATTGAAACAAACATACactagctaaatcccctcactggctctcttacgtatgagatgaggaccatgatggtaggagaagtttagtgaaagtcccagaacttccccttcttatccagaaatactgaatctctgaaagagctttggagattaatgccaccattaaagggttgaaataagcaggcactgtgacacttcttacaaacccatttaactggccactttggcctgtgcagaactcatattgttaccagaaaaaggggtctcgatcca"
# s=s.upper()
# print s
# '''
# '''''
# fa = open("./lambda_virus.fa")
# #fa = open("./alignment-sequence.fasta")
# lab=fa.read()
# lab=lab.upper()
# print lab
# '''
#
# long a = 0
# print a
'''
theFirstWord = "AAAAAAAAAA"
firstWordFile = open(theFirstWord + ".txt")
location = location + firstWordFile.readlines()
'''

import json
import re
import os
'''
def get_text(start_text, end, word):
    start = word.find(start_text)
    if start >= 0:
        start += len(start_text)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()


def get_word(i,seq):
    word = seq[i-1:i+9]
    return word

def buildLibrary(seq):
    for i in range (1, (len (seq) - 10)):
        word = get_word (i, seq)
        file= open("./library/%s"%word,"w+")
        contain = json.load (file)
        contain.append(i)
        json.dump (contain, file)
        file.close ()



fa = open("./lambda_virus.fa")
#fa = open("./alignment-sequence.fasta")
lab=fa.read()
#print lab

lab += ":"
sequences1 = get_text("\n",":",lab)
sequences1=re.sub(r'\s+','',sequences1)



'''
'''
f=[]
f.append(-1)
print "f"
print f
file=open("./233","w+")
json.dump(file,f)
file.close()

contain= []
r_file = open("./233","w+")
contain = json.load(r_file)
#print contain
r_file.close()


w_file = open("./233","w+")
contain.append("9")
json.dump(contain,w_file)
w_file.close()
'''
#file1 = open("./233","r+")
#e1 = json.load(file1)
#print e1
f=[]
file = open("./233","w+")
json.dump(f,file)
file.close()

file = open("./233","r+")
Dictionary = json.load(file)
file.close()



def match(seq):
    match_data = {}

    for i in range (1, (len (seq) - 9)):
        word = get_word (i, seq)
        with open ("./library/chr21/%s" % word, "a+") as data:
            data.seek (0)
            data = data.read ()
            # print data
            sub = data.split (" ")
            sub.pop ()
            # print sub
            for local in sub:
                local = int(local)
    match_data[word] += sub
    match_data[word].sort ()
    return match_data