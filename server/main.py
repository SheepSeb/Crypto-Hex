from typing import Optional
from fastapi import FastAPI
from AES import *
app = FastAPI()

@app.get("/aes/encrypt/{data}")
def aes_encrypt(data: str):
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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}