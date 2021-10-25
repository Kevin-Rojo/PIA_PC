from bs4 import BeautifulSoup as bs
import requests
import re
from urllib import request



url = "https://www.uanl.mx/enlinea/"
#url = input("Ingresa el link a analisar: ")
html = requests.get(url)
soup = bs(html.content, 'html.parser')

a= soup.find_all(href=re.compile("(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))"))


listOfDocs=[]
for document in a:
    listOfDocs.append(document['href'])

for doc in listOfDocs:
    while listOfDocs.count(doc)!=1:
        listOfDocs.remove(doc)

for doc in listOfDocs:
    filePatron=re.compile(r"(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))")
    fileType=filePatron.search(doc)
    print(doc)
    print(fileType.group(2))
    dir="I:\FCFM\GitHub\PIA_PC\DocumentGatering"+fileType.group(2)
    request.urlretrieve(doc,fileType.group(2))
