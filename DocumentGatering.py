from typing import Counter
from bs4 import BeautifulSoup as bs
import requests
import re
from urllib import request

#################################################################################################################################
#                           Funcion que permite descargar documento por medio de un url                                         #
#   Guarda los resultados para ralizar un reporte:                                                                              #
#       lista=GetWebDocumentsURL(url)                                                                                           #
#       lista=[Archivo1[url1,FileName1,FileType1],Archivo2[url2,FileName2,FileType2],...,Archivon[urln,FileNamen,FileTypen]]    #
#                                                                                                                               #
#   Argumentos:                                                                                                                 #
#       str:url->   URL que se va a analizar                                                                                    #
#   Variables:                                                                                                                  #
#       Tipo            Nombre          Descripcion                                                                             #
#       requests        html            Guarda la peticion hacia la url                                                         #
#       beautifulsoup   soup            Almacena el contenido del URL analizado                                                 #
#       beautifulsoup   a               Almacena todas las etiquetas a que contengan en su href el patron de documentos         #
#       list            listOfDocs      Almacena todos los URLs extraidos que contengn un documento para la descarga            #
#       list            Archivos        Almacena la lista que sera devuelta para realiar el reporte de Excel                    #
#       re              filePatron      Expresion regular para detectar URLs con Archivos de Tipo(pdf,excel,word,               #
#                                       powerponit, base de datos sql y texto)                                                  #
#       re              patronGroups    Almacena el resultado del analisis de la expresion regular                              #
#                                                                                                                               #
#################################################################################################################################
def GetWebDcumentsURL(url:str)->list:
    #Peticion a la URL y lectura del HTML en un objeto de BeautifulSoup
    html = requests.get(url)
    soup = bs(html.content, 'html.parser')
    #Se define le expresion regulrar para la busqueda de archivos conformada por 3 grupos (URL)(nombre del documento(Tipo de archivo))
    a= soup.find_all(href=re.compile("(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))"))


    listOfDocs=[]
    for document in a:
        listOfDocs.append(document['href'])

    for doc in listOfDocs:
        while listOfDocs.count(doc)!=1:
            listOfDocs.remove(doc)
    Archivos=[]
    for doc in listOfDocs:

        filePatron=re.compile(r"(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))")
        patronGroups=filePatron.search(doc)
        print(doc)
        print(patronGroups.group(2))

        dir="DocumentosExtraidos\\"+patronGroups.group(2)
        myfile = requests.get(doc, allow_redirects=True)
        open(dir, 'wb').write(myfile.content)
        tempList = [doc,patronGroups.group(2),patronGroups.group(3)]
        ##tempDict={'URL':doc,'FileName':patronGroups.group(2),'FileType':patronGroups.group(3)}
        Archivos.append(tempList)
    print(len(Archivos))
    if len(Archivos)>0:
        return Archivos
    else:
        print("no se han extraido Documentos")

#descarga Archivos de Paginas web desde una lista de URLs que recive por un directorio
def GetWebDcumentsListURL(urlDir:str)->list:

    # Inicia Abriendo el Archivo txt con la lista de URL a Analizar
    f = open(urlDir, "r")
    ListaArchivosTotales=[]
    for url in f:
        html = requests.get(url)
        soup = bs(html.content, 'html.parser')

        a= soup.find_all(href=re.compile("(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))"))

        listOfDocs=[]
        for document in a:
            listOfDocs.append(document['href'])

        for doc in listOfDocs:
            while listOfDocs.count(doc)!=1:
                listOfDocs.remove(doc)

        Archivos=[]
        for doc in listOfDocs:
            filePatron=re.compile(r"(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))")
            patronGorups=filePatron.search(doc)
            print(doc)
            print(patronGorups.group(2))
            dir="DocumentosExtraidos\\"+patronGorups.group(2)
            myfile = requests.get(doc, allow_redirects=True)
            open(dir, 'wb').write(myfile.content)
            #Lista con formato [URL, FileName, FileType]
            tempList = [doc,patronGorups.group(2),patronGorups.group(3)]
            #BORRAR#    tempDict={'URL':doc,'FileName':patronGorups.group(2),'FileType':patronGorups.group(3)}
            Archivos.append(tempList)
        print(len(Archivos))
        if len(Archivos)>0:
            tempList=[url,Archivos]
            ListaArchivosTotales.append(tempList)
        else:
            print("no se han extraido Documentos en" + url)
    f.close()
    #se regresa lista de listas para guardar el reporte FORMATO [URL1[Archivos1[],Archivos2[],],URL2[],...,URLn[],]
    return ListaArchivosTotales

GetWebDcumentsListURL("I:\\FCFM\\Github\\PIA_PC\\listaUrls.txt")
