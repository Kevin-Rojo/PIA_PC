import os
import openpyxl
import argparse
import time
import subprocess

import puertos
import EnvioCorreo


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
    command = f"powershell .\puertos.ps1 -ipaddress {ip} -port {ports}"
    res = subprocess.run(command, stdout=subprocess.PIPE)
    print(res)


if __name__ == "__main__":

    description = """Metodos de Ejeccion:
    [1].- WEB SCRAPING(Extraer emails de un sitio web)
    -Execution Example:main.py -op 1 -url "URL" -R "RUTA(ruta donde se almacenaran las imagenes)"

    [2].- Descarga De Documentos (Analizar metadatos de Imagenes)
    -Execution Example:main.py -op 2  -R "RUTA"
    
    [3].- ESCANEO CON SOCKET(Detecta los puertos si estan abiertos o cerrados)
    -Execution Example:main.py -op 3 -ip "IP" -begin "30" -end "50"
    
    [4].- IDENTIFICAR TECNOLOGIA DE WEBSITE(Ingresa un sitio web que desas analizar)
    -Execution Example:main.py -op 4 -url "URL"

    [5].- EXTRAER INFORMACION DE UN DOMINIO(Script para buscar información sobre un dominio)
    -Execution Example:main.py -op 5 -api "APIKEY" -organizacion "ORGANIZACION"
    
    [6].- OBTENCIÓN DE CLAVES HASH(Obtener la calve Hash de un carpeta) 
    -Execution Example:main.py -op 6 -R "RUTA"
    
    """
    parser = argparse.ArgumentParser(description="script", epilog=description)

    #parametros para ejecucion de script
    parser.add_argument("-mode", dest="mode", help="Designa el modo de ejecucion", default="Auto")
    parser.add_argument("-script", dest="script", help="Selecciona el script a Ejecutar individualmente")
    
    #Parametros Para Funcion EnvioCorreo.py
    parser.add_argument("--e", type=str,required=True,help="Destinatario")
    parser.add_argument("--m", type=str,required=True,help="Mensaje de correo")

    #Parametros Para Funcion DocumentGatering
    parser.add_argument("-source", dest="FilePath", help="Directorio de Urls")

    #parametros Para Funcion Puertos
    parser.add_argument("-ip", dest="ip",help="Direccion IP a Analizar")
    parser.add_argument("-port", dest="port",help="Puertos a analzar")

    #Parametros Para Funcion VirusTotal

    params = parser.parse_args()
    print(params.mode)
    print(description)

    if params.mode=="Auto" and params.script=="Email":
        #codigo para ejecucion en automatico de Email
        EnvioCorreo(args)
        validateMenu=False
    elif params.mode=="Auto" and params.script=="Documents":
        print("2")

        validateMenu=False
    elif params.mode=="Auto" and params.script=="WebMail":
        print("3")

        validateMenu=False
    elif params.mode=="Auto" and params.script=="VirusTotal":
        print("4")

        validateMenu=False
    elif params.mode=="Auto" and params.script=="ports":

        status_port(params.ip,params.port)

        validateMenu=False
    elif params.mode=="Manual":
        validateMenu=True
    else:
        print("parametros incorrectos...")
        print("saliendo")
        time.sleep(3)
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
    except:
        print("MODO DE EJECUCION INCORRECTO!")
        print(description)
        input("Presione cualquier tecla para continuar")
