import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import sys,os.path
import random
import copy
import pylab


populationsides= 100
geneNum=200


startNumberOf={}
startNumberOf["A"]=int(populationsides * 0.2)
startNumberOf["B"]=int(populationsides * 0.2)
startNumberOf["C"]=int(populationsides * 0.2)
startNumberOf["D"]=int(populationsides * 0.2)
startNumberOf["E"]=populationsides-startNumberOf["A"]-startNumberOf["B"]-startNumberOf["C"]-startNumberOf["D"]

number={}
number["A"]=[]
number["B"]=[]
number["C"]=[]
number["D"]=[]
number["E"]=[]



population=[]

for j in range (0,startNumberOf["A"]):
    population += "A"

for j in range (0,startNumberOf["B"]):
    population += "B"

for j in range (0,startNumberOf["C"]):
    population += "C"

for j in range (0,startNumberOf["D"]):
    population += "D"

for j in range (0,startNumberOf["E"]):
    population += "E"

def genetic(F1):

    F2 = copy.deepcopy(F1)

    for i in range (0,len(F1)):
        randomNumber = random.randint(0,len(F1)-1)
        #print randomNumber
        F2[i] = F1[randomNumber]

    return F2

def showThegenetic(F,sides):

    print F

    n = float(sides/100)
    print n
    '''
    A = float(F.count ("A")/sides*100)
    B = float(F.count ("B")/sides*100)
    C = float(F.count ("C")/sides*100)
    D = float(F.count ("D")/sides*100)
    E = float(F.count ("E")/sides*100)
    '''
    A = float (F.count ("A") )/n
    B = float (F.count ("B") )/n
    C = float (F.count ("C") )/n
    D = float (F.count ("D") )/n
    E = float (F.count ("E") )/n

    number["A"].append (A)
    number["B"].append (B)
    number["C"].append (C)
    number["D"].append (D)
    number["E"].append (E)


    print "A: ",A,"% B: ",B,"% C: ",C,"% D: ",D,"% E: ",E,"%"


F0 = population
F1 = F0
F2 = []
print "the F0: ",F0

showThegenetic(F0,populationsides)

for g in range (0,geneNum):

    F2 = genetic(F1)
    print "the F",g+1,": "
    showThegenetic(F2,populationsides)
    F1 = F2

workbook = xlsxwriter.Workbook("Expenses01.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write(0, 1 ,"A")
worksheet.write(0, 2 ,"B")
worksheet.write(0, 3 ,"C")
worksheet.write(0, 4 ,"D")
worksheet.write(0, 5 ,"E")

i=1
for vale in (number["A"]):
    worksheet.write (i, 1, vale)
    i+=1
i=1
for vale in (number["B"]):
    worksheet.write (i, 2, vale)
    i+=1
i=1
for vale in (number["C"]):
    worksheet.write (i, 3, vale)
    i+=1
i=1
for vale in (number["D"]):
    worksheet.write (i, 4, vale)
    i+=1
i=1
for vale in (number["E"]):
    worksheet.write (i, 5, vale)
    i+=1

for p in range (1,geneNum+2):
    worksheet.write (p, 0, p)

workbook.close()
