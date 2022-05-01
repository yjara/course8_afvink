import io

from flask import Flask,request,render_template
from Bio import Entrez
import mysql.connector

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook


conn = mysql.connector.connect(
    host="ensembldb.ensembl.org",
    user="anonymous",
    database="homo_sapiens_core_95_38"
)

app = Flask(__name__)


@app.route('/',methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        answer = request.form.get("answer", "")
        output = searchDis(answer)
        searchPubmed()
        return render_template("page1.html",output=output, answer=answer, size=len(output))
    else:
        return render_template("page1.html", output="",answer="",size=0)

def searchPubmed():
    fig, ax =plt.subplots(figsize=(6,4))


    pubMedDate = {}
    pubMedDate2 = {}

    Entrez.email = 'A.N.Other@example.com'
    date = 2000
    while date < 2020:
        handle = Entrez.esearch(db='pubmed', term='retina',mindate=f'{date}/01/01',maxdate=f'{date+4}/12/31')
        record = Entrez.read(handle)
        handle.close()
        pubMedDate[f'{date}-{date+4}'] = int(record.get('Count'))
        date = date + 4


    ax.bar(pubMedDate.keys(),pubMedDate.values(),color='r')
    plt.xticks(rotation=30,size=5)
    plt.ylabel("let's see",size=5)
    output = io.BytesIO()

def searchDis(test):
    cursor = conn.cursor()
    cursor.execute('''select description from gene where description like '%{}%\'limit 10'''.format(test))
    row = cursor.fetchall()
    regels = []
    for item in list(row):
        regel = str(item)[0:len(str(item))-3].strip("'()''").split(test)
        regels.append(regel)
    return regels

if __name__ == '__main__':
    app.run()
