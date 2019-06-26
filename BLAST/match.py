import json

def get_word(i,seq):
    word = seq[i-1:i+10]
    return word

def get_text(start_text, end, word):
    start = word.find(start_text)
    if start >= 0:
        start += len(start_text)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()

def matchSeq(seqInput):
    matchSeq=[]
    for i in range (1, (len (seqInput) - 10)):
        word = get_word(i,seqInput)
        file = open ("./library/%s"%chromName + "/%s"%word, "r+")
        contain = file.read()
        matchSeq.append(contain)
        file.close()
    sorted(matchSeq)
    return matchSeq

chromName="chr21"
seqInput=""
file=open("./search1.txt")
seqInput=file.read()
match = matchSeq(seqInput)
print "search1:  "+match

file=open("./search2.txt")
seqInput=file.read()
match = matchSeq(seqInput)
print "search2:  "+match









'''
seqInput=""
allmatchSeq=[]
score=[]

for i in range (1,25):
    chromName = ""
    if (i < 23):
        chromName = "chr%d"%i
    if (i == 23):
        chromName = "chrX"
    if (i == 24):
        chromName = "chrY"
    allmatchSeq[i]=matchSeq(seqInput)

for i in range (1,25):
    score[i]=len(allmatchSeq[i])

max=max(score)
chrom=""

for i in range (1,25):
    if score[i] == max:
        if (i < 23):
            chrom = "chr%d" % i
        if (i == 23):
            chrom = "chrX"
        if (i == 24):
            chrom = "chrY"
'''




'''
file = open("./Dictionary","r+")
Dictionary = json.load(file)

seq = "GGGCGGCGACCTCGCGGGTTTTCGCTATTTATGAAAATTTTCCGGTTTAAGGCGTTTCCGTTCTTCTTCGTCATAACTTAATGTTTTTATTTAAAATACCCTCTGAAAAGAAAGGAAACGACAGGTGCTGAAAGCGAGGC"
seq_dict = {}

sequences2=seq

for i in range(1,(len(sequences2)-10)):
    seq_dict[i] = get_word(i,sequences2)
    print i,seq_dict[i]


match_data = []
for i in range(1,((len(sequences2)-10)/10)):
    for (key, value) in Dictionary.items():
        if value.startswith(seq_dict[i]):
            print key
            match_data.append(key)

print(match_data)
'''

