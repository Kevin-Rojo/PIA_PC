import os
import openpyxl
import argparse
import time
import subprocess




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



def status_port(ip,ports):
   command = f"powershell .\puertos.ps1 -ipaddress {ip} -port {ports}"
   res = subprocess.run(command, stdout=subprocess.PIPE)
   print(res)



if __name__ == "__main__":

    description = """Ejecucion automatica: Main.py | Ejecucion manual: Main.py -mode Manual"""
    parser = argparse.ArgumentParser(description="script", epilog=description)
    parser.add_argument("-mode", dest="mode", help="Designa el modo de ejecucion", default="Auto")
    params = parser.parse_args() 
    print(params.mode)

    input()
    if params.mode=="Auto":
        #codigo para ejecucion en automatico
        print("paso 1")
        time.sleep(5)
        print("paso 2")
        time.sleep(5)
        print("paso 3")
        time.sleep(5)
        print("paso 4")
        time.sleep(5)
        print("paso 5")
        time.sleep(5)
        print("paso 6")
        validateMenu=False
    elif params.mode=="Manual":
        validateMenu=True

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
