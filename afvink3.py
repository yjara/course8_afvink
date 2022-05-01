from Bio import Entrez
import matplotlib.pyplot as plt

def searchPubmed():
    listCompounds = openFiles().split("\n")
    pubMedDate = {}
    Entrez.email = 'A.N.Other@example.com'

    startdate = 2010
    #https://biopython.org/docs/1.75/api/Bio.Entrez.html

    date = startdate
    bestCombie=""
    biggestHit=0
    for item in listCompounds:
        combie = f'{item} AND Alzheimer'
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

def openFiles():
    compoundsFileName ="c_oef.txt"
    geneFileName ="textmining/week 3/g_oef.txt"
    moleculairFileName = "textmining/week 3/m_oef.txt"
    compoundsFile = open(compoundsFileName,'r')
    compoundsList = compoundsFile.read()
    return compoundsList

if __name__ == '__main__':
    searchPubmed()
