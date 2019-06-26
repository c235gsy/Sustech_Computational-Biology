import time
import gc
import re
import string
import os

start = time.time ()

def get_word(i, seq):
    word = seq[i - 1:i + 10]
    return word

def get_text(start_text, end, word):
    start = word.find (start_text)
    if start >= 0:
        start += len (start_text)
        end = word.find (end, start)
        if end >= 0:
            return word[start:end].strip ()

def matrix(seq1, seq2, n1, n2, count):
    n = len (seq2)
    m = len (seq1)
    g = -5
    match = 3
    dismatch = -2
    # print seq1
    # print seq2

    matrix = []
    for i in range (0, m + 1):
        T = []
        for j in range (0, n + 1):
            T.append (0)
        matrix.append (T)
    for sii in range (0, m + 1):
        matrix[sii][0] = sii * g
    for sjj in range (0, n + 1):
        matrix[0][sjj] = sjj * g
    for siii in range (1, m + 1):
        for sjjj in range (1, n + 1):
            if seq1[siii - 1] == seq2[sjjj - 1]:
                q = match
            else:
                q = dismatch
            matrix[siii][sjjj] = max (matrix[siii - 1][sjjj] + g, matrix[siii - 1][sjjj - 1] + q,
                                      matrix[siii][sjjj - 1] + g, 0)
        sequ1 = [seq1[m - 1]]
        sequ2 = [seq2[n - 1]]
    # print sequ1
    # print sequ2
    pdd = []

    for x in range (0, m + 1):
        pdd.append (max (matrix[x]))
    maxValue = max (pdd)

    x = 0
    y = 0
    xlist = []
    ylist = []
    for i in range (0, m + 1):
        for j in range (0, n + 1):
            if matrix[i][j] == maxValue:
                xlist.append (i)
                ylist.append (j)

    for i in range (0, len (xlist)):
        x = xlist[i]
        y = ylist[i]
        end = count + x
        while matrix[x][y] != 0:
            if max (matrix[x][y - 1], matrix[x - 1][y - 1], matrix[x - 1][y]) == matrix[x - 1][y - 1]:
                x -= 1
                y -= 1
                sequ1.append (seq1[x - 1])
                sequ2.append (seq2[y - 1])
            elif max (matrix[x][y - 1], matrix[x - 1][y - 1], matrix[x - 1][y]) == matrix[x][y - 1]:
                y -= 1
                sequ1.append ('-')
                sequ2.append (seq2[y - 1])
            elif max (matrix[x][y - 1], matrix[x - 1][y - 1], matrix[x - 1][y]) == matrix[x - 1][y]:
                x -= 1
                sequ1.append (seq1[x - 1])
                sequ2.append ('-')
        start = count + x

        # print sequ1
        # print sequ2
        sequ1.reverse ()
        sequ2.reverse ()
        seque1 = string.join (sequ1, '')
        seque2 = string.join (sequ2, '')
        seque1 = seque1
        seque2 = seque2
        score = 0
        for k in range (0, len (seque1)):
            if seque1[k] == seque2[k]:
                score += 1
        score = float (score) / len (seque2)
        if score > 0.7 and len(seque1) > len(seq2)-10 and len(seque1) < len(seq2)+20:
            #aaaaaList=[n1,n2,start,end,seque1,seque2,score]
        #return  aaaaaList
            print n2, ":",seq2
            print "this program will alignment the insulin sequences of ", n1, " and ", n2
            print "start:", start, "end:", end
            print seque1
            print seque2
            print "the score of the ", n1, " and ", n2, " is ", score, "\n"

def match(seq,chrname):
    match_data = []

    for i in range (1, (len (seq) - 9)):
        word = get_word (i, seq)
        if os.path.exists("./library/%s/%s" % (chrname,word)):
            with open ("./library/%s/%s" % (chrname,word), "r") as data:
                data = data.read ()
                # print data
                sub = data.split (" ")
                sub.pop ()
                # print sub
                match_data += sub

    for j in range (0, len (match_data)):
        match_data[j] = int (match_data[j])
    match_data.sort ()
    return match_data

    # j=0
    # while j < (len(match_data)-2):
    #     if match_data[j+1]-match_data[j]>(len(seq)/2) and match_data[j+2]-match_data[j+1]>(len(seq)/2):
    #         del match_data[j]
    #     else:
    #         j+=1

def getSeed(match_data, seq):
    def cluster(match_data, a0, b0):
        a = []
        b = []
        c0 = (a0 + b0) / 2
        for i in range (0, len (match_data)):
            if match_data[i] <= c0 :
                a.append (match_data[i])
            else:
                b.append (match_data[i])
        a1 = average (a)
        b1 = average (b)
        return [a1,b1]

    def average(seq):
        total = 0
        for x in seq:
            total += x
        return total / len (seq)

    ''''
    p = 0
    while p < 5:
        j = 0
        while j < (len (match_data) - 2):
            if match_data[j+1] - match_data[j]>(len(seq)/5) and match_data[j+2]-match_data[j+1]>(len(seq)/5):
                del match_data[j]
            else:
                j += 1
        i = 0
        while i < (len (match_data) - 1):
            if match_data[j+1] - match_data[j]>(len(seq)/5):
                del match_data[j]
            else:
                i += 1
        p += 1

    '''
    #print match_data
    '''
    a0 = int (match_data[len(match_data)/4] )
    b0 = int (match_data[len(match_data)*3/4])
    #a0 = 31000000
    #b0 = 33000000
    c0 = int ((a0 + b0) / 2)
    a = []
    b = []


    for i in range (0, len (match_data)):
        if match_data[i] <= c0:
            a.append (match_data[i])
        else:
            b.append (match_data[i])

    a1 = average (a)
    b1 = average (b)

    while a0 != a1 or b0 != b1:
        a0 = a1
        b0 = b1
        list=cluster (match_data, a0, b0)
        a1 = list[0]
        b1 = list[1]
        print "a1,b1,a0,b0",a1,b1,a0,b0

    print "a1,b1,a0,b0", a1, b1, a0, b0

    seed = []
    seed.append (a1)
    seed.append (b1)
    return seed
    

    j = 0
    while j < (len (match_data) - 2):
        if match_data[j + 1] - match_data[j] > (len (seq)) and match_data[j + 2] - match_data[j + 1] > (
            len (seq)):
            del match_data[j+1]
        else:
            j += 1
    i = 0
    while i < (len (match_data) - 2):
        if match_data[i + 1] - match_data[i] > (len (seq) ):
            del match_data[i]
        else:
            i += 1
    '''
    j = 0
    while j < (len (match_data) - 2):
        if match_data[j + 1] - match_data[j] > (len (seq)) and match_data[j + 2] - match_data[j + 1] > (
                len (seq)):
            del match_data[j + 1]
        else:
            j += 1

    p = [0]
    for i in range (0, len(match_data)-1):
        a = int (match_data[i + 1])
        b = int (match_data[i])
        distance = (a - b)
        if distance > (len (seq)):
            p.append (i + 1)
    p.append(len(match_data))

    seed = []
    for i in range (0, len (p) - 1):
        seed.append (match_data[int (p[i]):int (p[i + 1])])
    # print "seed", seed

    seed_len = []
    for i in range (0, len (seed)):
        seed_len.append (len (seed[i]))
    # print "seed len",len(seed_len)

    q=0
    while q < len(seed_len):
        miss= int (seed[q][- 1])-int (seed[q][0])
        if miss > int(len(seq)+10) :
            del seed_len[q]
            del seed [q]
        else:
            q += 1
    # print seed
    # print "seed len", len(seed_len)

    fseed=[]
    while max(seed_len)>5:
        i = seed_len.index(max(seed_len))
        fseed.append(int (seed[i][0]))
        fseed.append(int (seed[i][- 1]))
        del seed_len[i]
        del seed[i]

    return fseed
############################################################
############################################################
############################################################
############################################################
############################################################

#fa = open ("./Dictionary/chr21", "r+")
#print "open file "
#seq = fa.read ()
#length = len(seq)
#print "get seq",length
#fa.close ()
#g2=seq[31722075:31722017]
#print "g2",g2
#g1=seq[32656344:32656247]
#print "g1",g1
'''
subDic={}
for i in range (1, (len (seq) - 6)):
    word = get_word (i, seq)
    subDic[word] = ""
    subDic[word] += ("%d" % (i) + " ")

for (key, value) in subDic.items ():
    with open ("./V_library/%s" % key, "a+") as r_file:
        r_file.write (value)

print "finish library"
print time.time() - start
'''
############################################################
############################################################
############################################################
############################################################
############################################################
'''
file = open ("./test.txt", "r")
test = file.read ()
test = test.upper()
test = re.sub (r'\s+', '', test)
test += ">"
SEQ1= get_text(">SEQ1",">",test)
SEQ2= get_text(">SEQ2",">",test)
#reSEQ1= SEQ1[::-1]
#reSEQ2= SEQ2[::-1]
file.close
'''
#SEQ1="ctaggagtacttaagacttagtttgatttgggctgggcgcggtggctcacgcctgtaatcccag"
#SEQ1=SEQ1.upper()

############################################################
############################################################
############################################################
############################################################
############################################################

def emmmmm(seqname,SEQ):
    #fDic = {}
    seqlength = len (SEQ)

    for i in range (1, 2):
        chromName = ""
        if (i < 23):
            chromName = "chr%d" % i
        if (i == 23):
            chromName = "chrX"
        if (i == 24):
            chromName = "chrY"
        if (i == 25):
            chromName = "chrMT"

        fa = open ("./Dictionary/"+chromName, "r")
        seq = fa.read ()
        fa.close ()

        matchData = match (SEQ,chromName)
        if len(matchData) != 0:
            seed = getSeed (matchData, SEQ)
            for j in range (0,len(seed),2):
                matrix (seq[int(seed[j] - 0.5 * seqlength):int(seed[j+1] + 0.5 * seqlength)],SEQ, chromName, seqname, int(seed[j] - 0.5 * seqlength))
    '''
    keyOfDic=sorted(fDic.keys())
    for key in keyOfDic:
        lll= fDic[key]
        n1 = lll(0)
        n2 = lll(1)
        start = lll(2)
        end = lll(3)
        seque1 = lll(4)
        seque2 = lll(5)
        score = lll(6)
        print "this program will alignment the insulin sequences of ", n1, " and ", n2, "\n"
        print "start:", start, "end:", end
        print seque1
        print seque2
        print "\n", "the score of the ", n1, " and ", n2, " is ", score, "\n"
    '''
#SEQ1="aaaaacatgacaaatgaaaaaaaatgggcaagactaaaacttttaaaaaagtttgagacagggtctcactctgtc"
#SEQ1=SEQ1.upper()

SEQ2="aaaaacatgacattgaaacaaaaatgggaaagactaaatcttttaaaagagtttgagacaggtctcactcatgtc"
SEQ2=SEQ2.upper()

#SEQ3="caaacaaaggaaataaccaagatcagaccagaactaaatgaaattgacacaacaacaacaacaacaaaaatacaa"
#SEQ3=SEQ3.upper()

#SEQ4="caaaaaaggaaatataccaagatctgaccagaccctaaatgaaagtgacacaacacaacaactacaaaaaaacaa"
#SEQ4=SEQ4.upper()



print ""
#emmmmm("SEQ1",SEQ1)
#emmmmm("reSEQ1",reSEQ1)
emmmmm("SEQ2",SEQ2)
#emmmmm("reSEQ2",reSEQ2)
#emmmmm("SEQ3",SEQ3)
#emmmmm("reSEQ1",reSEQ1)
#emmmmm("SEQ4",SEQ4)
#emmmmm("reSEQ2",reSEQ2)

print time.time () - start
gc.collect ()
