"""modulos"""
import os
import time
import sys
import csv
import openpyxl
import argparse


def menu():

    print('------------------menu-----------------------')
    print('Ingrese el numero de la accion a realizar')
    print("1. Analisis de encabezados de archivos.")
    print("2. Recopilacion de correos en pagina web")
    print("3. Analisis de puertos")
    print("4. Metadata de imagenes en una pagina web")
    print("5. recopilacion de archivos de una pagina web")
    print("6. ")


def GetMailWeb():
    print("Scripts de correo")

def GetMalwareVT():
    print("Scripts de analisis de malware")


def PortScan():
    print("Scripts Aalisis de puertos")


def GetMetadataWeb():
    print("Scripts Metadata Imagenes Web")


def GetFilesWeb():
    print("Scripts Extraer Archivos Web")

def InvalidOption() -> None:
    print("opcion invalida")

if __name__ == "__main__":

    descripcion = "Ejemplos de uso:"
    print('funcion main')

    switch_scripts = {
        1: GetMalwareVT,
        2: GetMailWeb,
        3: PortScan,
        4: GetMetadataWeb,
        5: GetFilesWeb,
    }
    while True:
        menu()
