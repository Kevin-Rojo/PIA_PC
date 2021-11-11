import os
from openpyxl import Workbook
import time
import subprocess
import re
import socket
import argparse
import EnvioCorreo
import AnalisisArchivos
import DocumentGatering
import BusquedaCorreosDoc

# Funcion para preguntar si se quiere realizar otra accion
def retryMenu():
    repetirMenu=True
    while repetirMenu:
        try:
            opcion = input("Quieres repetir el menu (Y/N)")
            if(opcion=="Y"):
                print("repitiendo menu")
                repetirMenu=False
                return True
            elif(opcion=="N"):
                print("saliendo")
                repetirMenu=False
                return False
        except:
            print("opcion incorrecta selecionar 'Y' o 'N'")


#funcion analisis de puertos
def status_port(ip,ports):
    for port in ports:
        command = f"powershell .\puertos.ps1 -ipaddress {ip} -port {int(port)}"
        res = subprocess.run(command, stdout=subprocess.PIPE)
        print(res)


def menu():
    print("----------Herramientas de CiberSeguridad-----------------")
    print("1. Envio de Correos")
    print("2. Descarga de documentos")
    print("3. Busqueda de correos")
    print("4. Analisis de Archivos")
    print("5. Analisis de Puertos")
    print("6. Salir")


def reporteExcel(lista):
    wb = Workbook()
    dest_filename = 'empty_book.xlsx'
    ws = wb.active
    for documentos in lista:
        print(documentos)
        for documento in documentos:
            print(documento)
            ws.append(documento)
    

if __name__ == "__main__":

    description = """Metodos de Ejeccion:
    [1]Phishing
    """
    parser = argparse.ArgumentParser(description="script", epilog=description)

    #parametros para ejecucion de script
    parser.add_argument("-mode", dest="mode", help="Designa el modo de ejecucion", default="Auto")
    parser.add_argument("-script", dest="script", help="Selecciona el script a Ejecutar individualmente", default="all")
    
    #Parametros Para Funcion EnvioCorreo.py
    parser.add_argument("-dest", dest="dest", type=str,help="Destinatario")

    #Parametros Para Funcion DocumentGatering
    parser.add_argument("-source", dest="FilePath", help="Directorio de Urls", default="listaUrls.txt")

    #parametros Para Funcion Puertos
    parser.add_argument("-ip", dest="ip",help="Direccion IP a Analizar", default="192.168.1.1")
    parser.add_argument("-port", dest="port",help="Puertos a analzar", default="8080,80")

    #Parametros Para Funcion VirusTotal
    parser.add_argument("-path", dest="dir",help="Directorio a Analizar")

    #Parametros Para Funcion BusquedaEmails
    parser.add_argument("-url", dest="url",help="Directorio a Analizar")

    params = parser.parse_args()
    
    # validateMenu=False=No mostrar el menu para ejecucion manual

    if params.mode=="Auto" and params.script=="Email":

        #codigo para ejecucion en automatico de Email
        EnvioCorreo.EnvioCorreo(params.dest.split(","))
        validateMenu=False

    elif params.mode=="Auto" and params.script=="Documents":
        print("2")
        document=DocumentGatering.GetWebDcumentsListURL(params.FilePath)

        #reporte Excel
        reporteExcel(document)
        validateMenu=False
    elif params.mode=="Auto" and params.script=="WebMail":
        
        BusquedaCorreosDoc.AnalisisCorreos(params.url)

        validateMenu=False
    elif params.mode=="Auto" and params.script=="VirusTotal":
        try:
            AnalisisArchivos.EscaneoDeArchivos(params.dir)
        except Exception as e:
            print("Lo senimos ha ocurrido un error: " + e)
        validateMenu=False
    elif params.mode=="Auto" and params.script=="Ports":

        status_port(params.ip,params.port.split(","))

        validateMenu=False
    elif params.mode=="Auto" and params.script=="all":
        #se lee el archivo de configuracion
        with open("Config.txt") as f:
            lineas = f.readlines()
        
        #se asigna el valor a las variables que serviran para la ejecucion del codigo
        
        #Separa la informacion importante del archivo de configuracion
        #Se usa .split para separar la informacion del :
        #En algunos casos se utilisa [:-1] para quitar el salto de linea que queda en el texto
        ip=lineas[4].split(":")[1][:-1]
        port=lineas[5].split(":")[1].split(",")
        ports=[]
        for p in port:
            ports.append(p[:-1])
        dest=lineas[3].split(",")
        FilePath=lineas[8].split(":")[1]
        url=lineas[6].split(":")[1]+":"+lineas[6].split(":")[2][:-1]
        dir=lineas[7].split(":")[1][:-1]


        EnvioCorreo.EnvioCorreo(dest)
        DocumentGatering.GetWebDcumentsListURL(FilePath)
        BusquedaCorreosDoc.AnalisisCorreos(url)
        AnalisisArchivos.EscaneoDeArchivos(dir)
        status_port(ip,ports)

        validateMenu=False
    elif params.mode=="Manual":
        validateMenu=True
    else:
        print("Faltan Parametros Ejemplos de uso:")
        print(description)
        time.sleep(5)
        validateMenu=False
    
    try:
        while validateMenu:
            validateOpcion=True
            while validateOpcion:
                try:
                    menu()
                    opcion =  int(input("Script: "))
                    if(opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6 or opcion==7):
                        print(opcion)
                        validateOpcion=False
                except:
                    print("opcion incorrecta selecione un numero entero del 1 al 6")

            if opcion==1 :                
                dest=input("Ingresa el correo destino: ")
                EnvioCorreo.EnvioCorreo(dest)
                validateMenu=retryMenu()
            elif opcion==2:
                url=input("ingrese una URL para buscar:")
                try:
                    DocumentGatering.GetWebDcumentsURL(url)
                except Exception as e:
                    print("A courrido un error: " + str(e))
                validateMenu=retryMenu()
            elif opcion==3:
                print("opcion 3")
                #inicio de opcion 3

                validateMenu=retryMenu()
            elif opcion==4:
                print("opcion 4")
                #inicio de opcion 4

                validateMenu=retryMenu()
            elif opcion==5:
                print("opcion 5")
                ip = input("Ingrese IP: ")
                ports = input("Ingrese el puerto: ")
                status_port(ip,ports)

                validateMenu=retryMenu()
            elif opcion==6:
                print("Saliendo...")
                validateMenu=False

    except Exception as e:
        print("Lo sentimos ha ocurrido un error: "+ str(e))
        print(description)
        input("Presione cualquier tecla para continuar")
