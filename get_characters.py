import json
import time
from hashlib import md5
import requests as rq

def get_characters(offset):
  public_key = '7e3bafcf3d5d13f3cad92a332e75c83c'
  private_key = 'ce3610571feb03fe377c0af702259e985735fbd6'
  ts = str(time.time())  
  hash_str = md5(f"{ts}{private_key}{public_key}".encode("utf8")).hexdigest()
  
  params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash_str,
        "orderBy": "name",
        "limit":100,
        "offset": offset
        
    } 
  try:
    r = rq.get('https://gateway.marvel.com:443/v1/public/characters', params=params) 
  except Exception as e:
    return False, e
  else:
    return r.json()


offset = 0
  
characters = get_characters(offset)

while characters['data']['count'] != 0 :
    
    for i in range(len(characters['data']['results'])):
        print("Character name:", characters['data']['results'][i]['name'], " - quantity of comics: ", characters['data']['results'][i]['comics']['available'])
          
    offset = offset + 100
    characters = get_characters(offset)
    
  
