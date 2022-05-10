import threading
import time
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
from datetime import datetime
import re

from Bio import Entrez, Medline

import matplotlib.pyplot as plt
besthitCompGene = 1
bestCombie = ""

def searchGeneMole(listMole,listGene):
    bestHitGeneMole = 0
    global bestCombieGeneMole
    print("start")
    indexTreath = 0
    countmis = 0
    countTotal = 0

    Entrez.email = 'A.C.Other@example.com'

    startdate = 2010
    maxDate = 2022
    # https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie = ""
    biggestHit = 0

    for item in range(0, len(listMole)):
        itemC = listMole[item]
        for itemM in listGene:
            countTotal = countTotal + 1
            try:
                combie = f'{itemC} AND {itemM}'
                handle = Entrez.esearch(db='pubmed', term=combie,
                                        mindate=f'{date}/01/01',
                                        maxdate=f'{maxDate}/12/31')
                record = Entrez.read(handle)
                handle.close()
                countCombo = int(record.get('Count'))
                if countCombo > bestHitGeneMole:
                    bestHitGeneMole = countCombo
                    bestCombieGeneMole = combie

            except:
                countmis = countmis + 1
    print("results>>combo3>>>>")
    print(bestCombieGeneMole)
    print(bestHitGeneMole)
    if countmis == 0:
        print("Percent miss: 0")
    else:
        print("Percent miss: " + str((countmis / countTotal) * 100))
    print("finish")

def searchGompGene(listComp,listGene):
    bestHitCompGene = 0
    global bestCombieCompGene
    print("start")
    indexTreath = 0
    countmis = 0
    countTotal = 0

    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    maxDate = 2022
    # https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie = ""
    biggestHit = 0

    for item in range(0, len(listComp)):
        itemC = listCompounds[item]
        for itemM in listGene:
            countTotal = countTotal + 1
            try:
                combie = f'{itemC} AND {itemM}'
                handle = Entrez.esearch(db='pubmed', term=combie,
                                        mindate=f'{date}/01/01',
                                        maxdate=f'{maxDate}/12/31')
                record = Entrez.read(handle)
                handle.close()
                countCombo = int(record.get('Count'))
                if countCombo > bestHitCompGene:
                    bestHitCompGene = countCombo
                    bestCombieCompGene = combie

            except:
                countmis = countmis + 1
    print("results>>combo1>>>>")
    print(bestCombieCompGene)
    print(bestHitCompGene)
    print("Hits: " + str(biggestHit))
    if countmis == 0:
        print("Percent miss: 0")
    else:
        print("Percent miss: " + str((countmis / countTotal) * 100))
    print("finish")

def searchGompMole(listComp,listMole):
    bestHitCompMole = 0
    global bestCombieCompMole
    print("start")
    indexTreath = 0
    countmis = 0
    countTotal = 0

    Entrez.email = 'A.B.Other@example.com'

    startdate = 2010
    maxDate = 2022
    # https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie = ""
    biggestHit = 0

    for item in range(0, len(listComp)):
        itemC = synonyms(listCompounds[item]) # listCompounds[item]
        for itemM in listMole:
            countTotal = countTotal + 1
            try:
                combie = f'({itemC}) AND ({synonyms(itemM)})'
                handle = Entrez.esearch(db='pubmed', term=combie,
                                        mindate=f'{date}/01/01',
                                        maxdate=f'{maxDate}/12/31')
                record = Entrez.read(handle)
                handle.close()
                countCombo = int(record.get('Count'))
                if countCombo > bestHitCompMole:
                    bestHitCompMole = countCombo
                    bestCombieCompMole = combie

            except:
                countmis = countmis + 1
    print("results>>>>combo2>>")
    print(bestCombieCompMole)
    print(bestHitCompMole)
    print("Hits: " + str(biggestHit))
    if countmis == 0:
        print("Percent miss: 0")
    else:
        print("Percent miss: " + str((countmis / countTotal) * 100))
    getIDs(bestCombieCompMole)
    articles(getIDs(bestCombieCompMole))
    print("finish")

def openFiles():
    compoundsFileName = "c_oef.txt"
    geneFileName = "g_oef.txt"
    moleculairFileName = "m_oef.txt"

    compoundsFile = open(compoundsFileName, 'r')
    moleculairFile = open(moleculairFileName, 'r')
    geneFile = open(geneFileName, 'r')

    moleculairList = moleculairFile.read().split("\n")
    compoundsList = compoundsFile.read().split("\n")
    geneList = less(geneFile)
    return compoundsList, moleculairList, geneList


def less(genefile):
    geneList = []
    while True:
        line = genefile.readline()
        if len(re.sub(r"[0-9\n\s\t.,]", "", line.strip())) == 3:
            geneList.append(line.strip())
        if not line:
            break
    print(geneList)
    return geneList

def run3Threads():
    t1 = threading.Thread(target=searchGompGene,
                          args=(listCompounds, geneList))
    t2 = threading.Thread(target=searchGompMole,
                          args=(listCompounds, listMolecular))
    t3 = threading.Thread(target=searchGeneMole,
                          args=(listMolecular, geneList))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("time:")
    print(datetime.now())

def run6Threads():
    print(datetime.now())
    int2 = int(len(listCompounds) / 2)
    comppounds1 = listCompounds[0, int2]
    comppounds2 = listCompounds[int2, int(len(listCompounds))]
    t1 = threading.Thread(target=searchGompGene,
                          args=(comppounds1, geneList))
    t2 = threading.Thread(target=searchGompMole,
                          args=(comppounds1, listMolecular))
    t3 = threading.Thread(target=searchGeneMole,
                          args=(listMolecular, geneList))

    t4 = threading.Thread(target=searchGompGene,
                          args=(comppounds2,
                                geneList))
    t5 = threading.Thread(target=searchGompMole,
                          args=(comppounds2, listMolecular))


    t1.start()
    t2.start()
    t3.start()

    t4.start()
    t5.start()


    t1.join()
    t2.join()
    t3.join()

    t4.join()
    t5.join()
    print("time:")
    print(datetime.now())

def synonyms(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    stringSyn = str(set(synonyms)).replace("', '"," OR ").replace("{'","").replace("'}","")
    if stringSyn == 'set()':
        stringSyn = word
    return stringSyn

def getIDs(combie):
    startdate = 2010
    maxDate = 2022
    date = startdate
    handle = Entrez.esearch(db='pubmed', term=combie,
                            mindate=f'{date}/01/01',
                            maxdate=f'{maxDate}/12/31')
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]
    print(idlist)
    return idlist

def articles(combie):
    gi_str = ",".join(combie)
    handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb",
                           retmode="text")
    text = handle.read()
    print(text)

if __name__ == '__main__':
    listCompounds, listMolecular, geneList = openFiles()
    print(datetime.now())
    run3Threads()
    articles(bestCombieCompGene)
    print(bestCombieCompGene)
    print(bestCombieCompMole)
    print(bestCombieGeneMole)
