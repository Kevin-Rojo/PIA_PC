#Se importaron los módulos argparse y subprocess de python para las diferentes acciones a continuación
import argparse
import subprocess

#Se ejecuta el comando desde powershell para la obtención del estado del puerto 
def status_port(ip,ports):
   command = f"powershell .\puertos.ps1 -ipaddress {ip} -port {ports}"
   res = subprocess.run(command, stdout=subprocess.PIPE)
   print(res)

#Funcion principal
if __name__ == "__main__":
   ip = input("Ingrese IP: ")
   ports = input("Ingrese el puerto: ")
   status_port(ip,ports)
