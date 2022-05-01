from Bio import Entrez
import matplotlib.pyplot as plt

def searchPubmed():
    pubMedDate = {}
    pubMedDate2 = {}

    Entrez.email = 'A.N.Other@example.com'

    startdate = 1970
    enddate = 2020

    date = startdate
    while date < enddate:
        handle = Entrez.esearch(db='pubmed', term='retina',mindate=f'{date}/01/01',maxdate=f'{date+4}/12/31')
        record = Entrez.read(handle)
        handle.close()
        handle2 = Entrez.esearch(db='pubmed', term='testosterone',
                                mindate=f'{date}/01/01',
                                maxdate=f'{date + 4}/12/31')
        record2 = Entrez.read(handle2)
        handle2.close()

        pubMedDate2[f'{str(date)[2:4]}-{str(date + 5)[2:4]}'] = int(record2.get('Count'))
        pubMedDate[f'{str(date)[2:4]}-{str(date+5)[2:4]}'] = int(record.get('Count'))
        date = date + 5

    # plotting the points
    plt.plot(pubMedDate.keys(), pubMedDate.values(),color='r', label='retina')
    plt.plot(pubMedDate2.keys(), pubMedDate2.values(), color='g', label='testos')
    # naming the x axis
    plt.xlabel('jaar')
    plt.xticks(rotation=90,fontsize=6)
    # naming the y axis
    plt.ylabel('hits')
    # giving a title to my graph
    plt.title(f'Hits per 5 jaar, van {startdate} tot {enddate}')
    # function to show the plot
    plt.show()

if __name__ == '__main__':
    searchPubmed()