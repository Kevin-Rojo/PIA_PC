#Importamos librerias

#Solicitudes a paginas web
import requests

#Expresiones regulares
import re

#acceso a la interfaz BSD socket
import socket

#Pasar argumentos
import argparse

#Pasamos el argumento --l para introducir el url de la pagina web
parser = argparse.ArgumentParser()
parser.add_argument("--l", type=str,required=True,help="URL")
args=parser.parse_args()
url = args.l

#Hacemos un request a la url introduccida obligatoriamente por el argumento
req = requests.get(url)
if req.status_code != 200:
    exit()

# Se utilizan las expresiones regulares para la busqueda de correos
RegEx = "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
# re.findall busca todas las coincidencias posibles en la secuencia anterior
# .text convierte el codigo html a texto legible
emails = set(re.findall(RegEx, req.text, re.I))

# Revisamos si la variable emails no esta vaia
# En dado caso de que no se hayan encontrado correos, se mostrara un mensaje
# Caso contrario se guardaran los correos encontrados en un archivo txt
if len(emails) == 0:
    print("No se encontraron correos electronicos")
else:
# Se crea un archivo de texto en donde se guardaran los correos
    f = open("correos.txt", "w")
    for i in emails:

        regDominio=re.compile(r'([a-z0-9\.\-+_]+)[@]([a-z0-9\.\-+_]+\.[a-z]+)')
        dominio=regDominio.search(i)
        print(i)
        try:
            print(socket.gethostbyname(dominio.group(2)))
            f.write(i + "\t"+ dominio.group(2) + "\t"+ socket.gethostbyname(dominio.group(2)) + "\n")
        except:
            print("Dominio invalido")
    f.close()
    print("\n Hecho")