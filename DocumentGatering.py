from typing import Counter
from bs4 import BeautifulSoup as bs
import requests
import re
#from urllib import request
"""
    Orden para Funcion Manual

    Archivos: [
        archivo1[
            URL, NombreDeArchivo, TipoArchivo
        ],
        archivo2[
            URL, NombreDeArchivo, TipoArchivo
        ], 
        archivo3[
            URL, NombreDeArchivo, TipoArchivo
        ], 
        archivo4[
            URL, NombreDeArchivo, TipoArchivo
        ],  
    ]

    ListaArchivosTotales: [
        Archivos1: [
            archivo1[
                URL1, NombreDeArchivo, TipoArchivo
            ],
            archivo2[
                URL1, NombreDeArchivo, TipoArchivo
            ], 
            archivo3[
                URL1, NombreDeArchivo, TipoArchivo
            ], 
            archivo4[
                URL1, NombreDeArchivo, TipoArchivo
            ],  
        ],
        Archivos2: [
            archivo1[
                URL2, NombreDeArchivo, TipoArchivo
            ],
            archivo2[
                URL2, NombreDeArchivo, TipoArchivo
            ], 
            archivo3[
                URL2, NombreDeArchivo, TipoArchivo
            ], 
            archivo4[
                URL2, NombreDeArchivo, TipoArchivo
            ],  
        ]
    ]
"""

#################################################################################################################################
#                           Funcion que permite descargar documento por medio de un url                                         #
#   Guarda los resultados para ralizar un reporte:                                                                              #
#       lista=GetWebDocumentsURL(url)                                                                                           #
#       lista2=[Archivo1[url1,FileName1,FileType1],Archivo2[url2,FileName2,FileType2],...,Archivon[urln,FileNamen,FileTypen]]   #                                                    #
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

    #   (URL)(NombreArchivo(tipo de Archivo))
    links= soup.find_all(href=re.compile("(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))"))#etiqueta < href="">

    #   [<a1>['href'="link1"], <a2>['href'="link2"], <a3>['href'="link3"]]  href=ruta del documento
    lista_Documentos=[]# Aqui se guardan los links para la descarga
    for document in links:
        lista_Documentos.append(document['href'])
    
    # lista_Documentos=[ruta1, ruta2 , ruta3, ruta1]
    #Limpia documentos Repetidos
    for documento in lista_Documentos:
        while lista_Documentos.count(documento)!=1:
            lista_Documentos.remove(documento)
    # lista_Documentos=[ruta2 , ruta3, ruta1]



    Archivos=[] #Almacena la informacion de los documentos descargados [[url,nombre del archivo, tipo del archivo],...]
    
    #en este ciclo se copian todos los documentos encntrados en la lista "lista_Documentos" y se guardan en la carpeta DocumentosExtraidos
    for documento in lista_Documentos:
        
        #se declara la expresion regulrar para separar la informacion en 3 grupos:
        #grupo1="ruta del archivo(link)" grupo2="nombre del archivo con extension" groupo3="extension del archivo"
        filePatron=re.compile(r"(.+[a-z0-9]\/)+(.+\.(pdf|docx|doc|PDF|xlsx|xls|ppt|txt|sql))")

        #busca el patron dentro de la ruta completa donde se encuentra el documento
        patronGroups=filePatron.search(documento)

        #nombra la ruta donde se guardara el archivo en este caso es /DocumentosExtraidos/NombreDelArchivo.Extension
        dir="DocumentosExtraidos\\"+patronGroups.group(2) #ruta y nombre del archivo a copiar

        documento_descargado = requests.get(documento, allow_redirects=True)


        open(dir, 'wb').write(documento_descargado.content)
        #[URL, NombreDeArchivo, Tipo]
        tempList = [documento,patronGroups.group(2),patronGroups.group(3)]

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

        lista_Documentos=[]
        for document in a:
            lista_Documentos.append(document['href'])

        for doc in lista_Documentos:
            while lista_Documentos.count(doc)!=1:
                lista_Documentos.remove(doc)

        Archivos=[]
        for doc in lista_Documentos:
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

