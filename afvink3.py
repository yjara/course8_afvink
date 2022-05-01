import threading
import time
from datetime import datetime

from Bio import Entrez
import matplotlib.pyplot as plt

def treadSearch():
    countmis = 0
    print(datetime.now().minute)
    listCompounds, listMolecular, geneList = openFiles()
    pubMedDate = {}
    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    # https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie = ""
    biggestHit = 0

    aantalComboPerThread = 25
    size = int(len(listCompounds)/aantalComboPerThread)
    if size < 2:
        size = 2

    threadList = []
    start = 0
    print(size)
    for item in range(0,size):
        print("thread start")
        threadList.append(threading.Thread(target=searchPubmed,args=(start,(item+1)*aantalComboPerThread,listCompounds, listMolecular, geneList)))
        start = (item+1)*aantalComboPerThread
        time.sleep(0.1)
    print("treat start")
    threadList.append(threading.Thread(target=searchPubmed,args=(start,start+(len(listCompounds)%aantalComboPerThread),listCompounds, listMolecular, geneList)))
    for item in range(0,size+1):
        threadList[item].start()
        time.sleep(15) #between 50-60 misses   #hoogste 71 meeste rond 55  #sleep van 20 gaf gemiddeld 40-45 dus 30-40%  #25 is nice
       # time.sleep(2)
       # time.sleep(5)
    for ite in range(0,size+1):
        threadList[ite].join()
        time.sleep(0.2)
    print("done")
    print(datetime.now().minute)


def searchPubmed(start,end, listCompounds, listMolecular, listGenes ):
    countmis = 0
    countTotal = 0
   # listCompounds, listMolecular, listGenes = openFiles()
    pubMedDate = {}
    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    maxDate = 2022
    #https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie=""
    biggestHit=0

    goodhits = []
    for item in range(start,end):
        itemC = listCompounds[item]
        for itemM in listGenes:
            try:
                combie = f'{itemC} AND {itemM}'
                handle = Entrez.esearch(db='pubmed',term=combie,mindate=f'{date}/01/01',maxdate=f'{maxDate}/12/31')
                record = Entrez.read(handle)
                handle.close()
                countCombo = int(record.get('Count'))
                time.sleep(0.2) #between 50 - 60 misses
               # time.sleep(2)
                if countCombo > biggestHit:
                    biggestHit = countCombo
                    bestCombie = combie
                countTotal = countTotal + 1
            except:
                countmis = countmis + 1
    print("Combo: "+bestCombie)
    print("Hits: " + str(biggestHit))
    print("time: " + str(datetime.now().minute))
    print("mis: " + str(countmis))
    return bestCombie

def openFiles():
    compoundsFileName ="c_oef.txt"
    geneFileName ="g_oef.txt"
    moleculairFileName = "m_oef.txt"

    compoundsFile = open(compoundsFileName,'r')
    moleculairFile = open(moleculairFileName,'r')
    geneFile = open(geneFileName,'r')




    moleculairList = moleculairFile.read().split("\n")
    compoundsList = compoundsFile.read().split("\n")
    geneList = less(geneFile)
    return compoundsList,moleculairList,geneList

def less(genefile):
    geneList = []
    while True:
        line = genefile.readline()
        if len(line.replace(".","").strip()) == 3:
            geneList.append(line.strip())
        if not line:
            break
    print(geneList)
    return geneList


if __name__ == '__main__':
    openFiles()
    treadSearch()
