

from __future__ import print_function
import os
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

#path_file = input("ingrese la ubicacion del archivo a analizar")

#print(os.listdir('I:\FCFM\GitHub\PIA_PC\Prueba API VT\API'))

with open('Prueba API VT/APIKEY.txt', "r") as f:
    API_KEY = f.readline()

with open('../../archivo de prueba/NoVirus.txt', "rb") as f:
    file_hash = hashlib.md5(f.read()).hexdigest()

vt = VirusTotalPublicApi(API_KEY)

response = vt.get_file_report(file_hash)
print(json.dumps(response, sort_keys=False, indent=4))


if response['results']['positives'] > (response['results']['total']/2):
    print("malware")