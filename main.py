import os
import openpyxl
import argparse
import time
import subprocess
import re
import socket

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
        DocumentGatering.GetWebDcumentsListURL(params.FilePath)
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

        status_port(params.ip,params.port)

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
                    opcion =  int(input("Que script desea ejecutar"))
                    if(opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6 or opcion==7):
                        print(opcion)
                        validateOpcion=False
                except:
                    print("opcion incorrecta seleciones un numero entero del 1 al 7")

            if opcion==1 :
                print("opcion 1")
                #inicio de opcion 1

                validateMenu=retryMenu()
            elif opcion==2:
                print("opcion 2")
                #inicio de opcion 2

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
                print("opcion 6")
                #inicio de opcion 6

                validateMenu=retryMenu()
            elif opcion==7:
                print("Saliendo...")
                validateMenu=False
    except Exception as e:
        print("MODO DE EJECUCION INCORRECTO!")
        print(description)
        input("Presione cualquier tecla para continuar")
