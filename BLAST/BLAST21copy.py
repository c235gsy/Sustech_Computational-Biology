import time
import gc
import re
import string

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
    dismatch = -3
    # print seq1
    # print seq2

    print "this program will alignment the insulin sequences of ", n1, " and ", n2, "\n"
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
        global score
        score = 0
        for k in range (0, len (seque1)):
            if seque1[k] == seque2[k]:
                score += 1
        score = float (score) / len (seque2)
        if score > 0.8:
            print "start:", start, "end:", end
            print seque1
            print seque2
            print "\n", "the score of the ", n1, " and ", n2, " is ", score, "\n"


def match(seq):
    match_data = []

    for i in range (1, (len (seq) - 9)):
        word = get_word (i, seq)
        with open ("./chr21/%s" % word, "a+") as data:
            data.seek (0)
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
            if match_data[i] <= c0:
                a.append (match_data[i])
            else:
                b.append (match_data[i])
        a1 = average (a)
        b1 = average (b)
        return [a1, b1]

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

    # print match_data
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
    for i in range (0, len (match_data) - 1):
        a = int (match_data[i + 1])
        b = int (match_data[i])
        distance = (a - b)
        if distance > (len (seq)):
            p.append (i + 1)
    p.append (len (match_data))

    seed = []
    for i in range (0, len (p) - 1):
        seed.append (match_data[int (p[i]):int (p[i + 1])])
    # print "seed", seed

    seed_len = []
    for i in range (0, len (seed)):
        seed_len.append (len (seed[i]))
    # print "seed len",len(seed_len)


    q = 0
    while q < len (seed_len):
        miss = int (seed[q][- 1]) - int (seed[q][0])
        if miss > int (len (seq) + 10):
            del seed_len[q]
            del seed[q]
        else:
            q += 1
    # print seed
    # print "seed len", len(seed_len)



    i = seed_len.index (max (seed_len))
    seed_s1 = int (seed[i][0])
    seed_o1 = int (seed[i][- 1])
    del seed_len[i]
    del seed[i]

    i = seed_len.index (max (seed_len))
    seed_s2 = int (seed[i][0])
    seed_o2 = int (seed[i][- 1])
    del seed_len[i]
    del seed[i]

    i = seed_len.index (max (seed_len))
    seed_s3 = int (seed[i][0])
    seed_o3 = int (seed[i][- 1])
    del seed_len[i]
    del seed[i]

    return [seed_s1, seed_o1, seed_s2, seed_o2, seed_s3, seed_o3]


############################################################
############################################################
############################################################
############################################################
############################################################
############################################################


fa = open ("./Dictionary/chr21", "r+")
print "open file "
seq = fa.read ()
length = len (seq)
print "get seq", length
fa.close ()
# g2=seq[31722075:31722017]
# print "g2",g2
# g1=seq[32656344:32656247]
# print "g1",g1
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

file = open ("./test.txt", "r+")
test = file.read ()
test = test.upper ()
test = re.sub (r'\s+', '', test)
test += ">"
SEQ1 = get_text (">SEQ1", ">", test)
SEQ2 = get_text (">SEQ2", ">", test)
# SEQ1= SEQ1[::-1]
# SEQ2= SEQ2[::-1]
file.close

# SEQ1="ctaggagtacttaagacttagtttgatttgggctgggcgcggtggctcacgcctgtaatcccag"
# SEQ1=SEQ1.upper()

print "SEQ1: ", SEQ1

len1 = len (SEQ1)

matchData = match (SEQ1)
print "match1", len (matchData)

seed = getSeed (matchData, SEQ1)

print seed

matrix (seq[int (seed[0] - 3 * len1):int (seed[1] + 3 * len1)], SEQ1, "chr21", "SEQ1", int (seed[0] - 3 * len1))

matrix (seq[int (seed[2] - 3 * len1):int (seed[3] + 3 * len1)], SEQ1, "chr21", "SEQ1", int (seed[2] - 3 * len1))

matrix (seq[int (seed[4] - 3 * len1):int (seed[5] + 3 * len1)], SEQ1, "chr21", "SEQ1", int (seed[4] - 3 * len1))

# SEQ2="ctagcagtacttaagattagctttgaatttgagctgcgcgcgttggctaacgcctgtaatccag"
# SEQ2=SEQ2.upper()

print "SEQ2: ", SEQ2

len2 = len (SEQ2)

matchData = match (SEQ2)
# print "match2",matchData
seed = getSeed (matchData, SEQ2)

print seed

matrix (seq[int (seed[0] - 3 * len1):int (seed[1] + 3 * len1)], SEQ2, "chr21", "SEQ2", int (seed[0] - 3 * len1))

matrix (seq[int (seed[2] - 3 * len1):int (seed[3] + 3 * len1)], SEQ2, "chr21", "SEQ2", int (seed[2] - 3 * len1))

matrix (seq[int (seed[4] - 3 * len1):int (seed[5] + 3 * len1)], SEQ2, "chr21", "SEQ2", int (seed[4] - 3 * len1))

print time.time () - start

gc.collect ()
