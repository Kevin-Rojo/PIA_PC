import requests
import re
import socket

url = input("Ingrese la url: ")
def BusquedaCorreos():
    # Se revisa el estado la pagina
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
