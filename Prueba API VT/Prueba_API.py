#api Key 529aad229b636a3bfab6f6c9a3ecc25dcee6efb3e0c93200d95a4e2e3278af5e

from __future__ import print_function
import os
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

API_KEY = '529aad229b636a3bfab6f6c9a3ecc25dcee6efb3e0c93200d95a4e2e3278af5e'
path_file = input("ingrese la ubicacion del archivo a analizar")

print(os.listdir('../../archivo de prueba/EICAR.com'))


with open('I:/FCFM/archivo de prueba/EICAR.com', "rb") as f:
    file_hash = md5(f.read()).hexdigest()

EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
#print(EICAR)
file_MD5 = hashlib.md5(EICAR).hexdigest()
input()
vt = VirusTotalPublicApi(API_KEY)

response = vt.get_file_report(file_hash)
print(json.dumps(response, sort_keys=False, indent=4))