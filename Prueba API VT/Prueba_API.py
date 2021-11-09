from typing import Callable
import base64
import time

import os
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
from virus_total_apis.api import ApiError

#path_file = input("ingrese la ubicacion del archivo a analizar")

#print(os.listdir('I:\FCFM\GitHub\PIA_PC\Prueba API VT\API'))

#def encode_decode_bytes(
#    byte_message: bytes, encode_fn: Callable[[bytes], bytes]
#) -> bytes:
#    return encode_fn(byte_message)

#def decode_file(path: str) -> bytes:    
#    file_to_encode = open(path, "rb")
#    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


with open('encode_APIKEY.txt', "r") as f:
    API_KEY = f.readline()
    print(type(API_KEY))
    API_KEY = base64.b64decode(API_KEY)

print(API_KEY.decode("utf-8")[1:])

def EscaneoDeArchivos(Direcotrio,API_KEY):
    archivos=os.listdir(Direcotrio)
    for archivo in archivos:
        print(archivo)
        try:
            full_Directorio=r""+str(Direcotrio)+"\\"+str(archivo)
            with open(full_Directorio, "rb") as f:
                hash_Archivo = hashlib.md5(f.read()).hexdigest()

            vt = VirusTotalPublicApi(API_KEY.decode("utf-8")[1:])

            respuesta = vt.get_file_report(hash_Archivo)
            print(json.dumps(respuesta, sort_keys=False, indent=4))


            if respuesta['response_code'] == 200:
                if respuesta['results']['response_code'] == 0:
                    print("archivo no disponible en la base de datos, puesto en cola para analisis publico")
                else:
                    if respuesta['results']['positives'] > 1:
                        print("malware")
        except Exception as e:
            print("ocurrio un error: " + str(e))
        time.sleep(25)

EscaneoDeArchivos("C:\\Users\\DCI\\Documents\\GitHub\\",API_KEY)