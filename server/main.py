import urllib.parse
from typing import Optional
from fastapi import FastAPI
from AES import *
import hashimg
app = FastAPI()


def url_parse(data):
    return urllib.parse.unquote(data)



@app.get("/set-profile/{data}")
def set_profile(data: str):
    data = url_parse(data)
    print(data)
    hash = hashimg.hash_img_url(data)
    print (hash)
    payload = {
        "data":hash
    }
    return payload

@app.get("/aes/encrypt/{data}")
def aes_encrypt(data: str):
    data = url_parse(data)
    key = "1234"
    AESCipher(key)
    send = ciph.encrypt(data)
    payload = {
        "data":send
    }
    return payload

@app.get("/aes/decrypt/{data}")
def aes_decrypt(data: str):
    key = "1234"
    AESCipher(key)
    send = ciph.decrypt(data)
    payload = {
        "data":send
    }
    return payload


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/")
def read_root():
    return {"Hello": "World"}