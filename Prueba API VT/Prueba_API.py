from typing import Callable
import base64

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
    API_KEY = hashlib.md5(API_KEY.encode())


print(API_KEY)

input()
with open('../../archivo de prueba/NoVirus.txt', "rb") as f:
    file_hash = hashlib.md5(f.read()).hexdigest()

vt = VirusTotalPublicApi(API_KEY)

response = vt.get_file_report(file_hash)
print(json.dumps(response, sort_keys=False, indent=4))


if response['results']['positives'] > (response['results']['total']/2):
    print("malware")