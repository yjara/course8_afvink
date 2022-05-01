from datetime import datetime

from Bio import Entrez
import matplotlib.pyplot as plt

def treadSearch():
    print(datetime.now().minute)
    listCompounds, listMolecular = openFiles()
    pubMedDate = {}
    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    # https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie = ""
    biggestHit = 0
    for itemC in listCompounds:
        for itemM in listMolecular:
            combie = f'{itemC} AND {itemM}'
            handle = Entrez.esearch(db='pubmed', term=combie,
                                    mindate=f'{date}/01/01')
            record = Entrez.read(handle)
            handle.close()
            countCombo = int(record.get('Count'))
            if countCombo > biggestHit:
                biggestHit = countCombo
                bestCombie = combie
    print(bestCombie)
    print(biggestHit)
    print("time:")
    print(datetime.now().minute)


def searchPubmed():
    print(datetime.now().minute)
    listCompounds, listMolecular = openFiles()
    pubMedDate = {}
    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    #https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie=""
    biggestHit=0
    for itemC in listCompounds:
        for itemM in listMolecular:
            combie = f'{itemC} AND {itemM}'
            handle = Entrez.esearch(db='pubmed', term=combie,
                                    mindate=f'{date}/01/01')
            record = Entrez.read(handle)
            handle.close()
            countCombo = int(record.get('Count'))
            if countCombo > biggestHit:
                biggestHit = countCombo
                bestCombie = combie
    print(bestCombie)
    print(biggestHit)
    print("time:")
    print(datetime.now().minute)

def openFiles():
    compoundsFileName ="c_oef.txt"
    geneFileName ="textmining/week 3/g_oef.txt"
    moleculairFileName = "m_oef.txt"
    compoundsFile = open(compoundsFileName,'r')
    moleculairFile = open(moleculairFileName,'r')
    moleculairList = moleculairFile.read().split("\n")
    compoundsList = compoundsFile.read().split("\n")
    return compoundsList,moleculairList

if __name__ == '__main__':
    searchPubmed()
