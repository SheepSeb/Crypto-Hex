import urllib.parse
from typing import Optional
from fastapi import FastAPI
from AES import *
from rsa import *
import hashimg
import dbtes as mongo
app = FastAPI()


def url_parse(data):
    return urllib.parse.unquote(data)

def google_img(url):
    return 'https://lh3.googleusercontent.com/ogw/' + url


@app.get("/set-profile/{data}")
def set_profile(data: str):
    data = url_parse(data)
    data = google_img(data)
    hash = hashimg.hash_img_url(data)
    payload = {
        "data":hash
    }
    return payload

@app.get('/send/{email}/{alg}/{password}/{username}/{picture}')
def email(email:str,picture:str,alg:int,password:str):

    pw = url_parse(password)
    hash = send = ''

    if alg == 1:
        picture = url_parse(picture)
        picture = google_img(picture)
        hash = hashimg.hash_img_url(picture)
        ciph = AESCipher(hash)
        send = ciph.encrypt(pw)
    else:
        hash = RSA.generate(2048)
        send = rsa_encrypt(pw, hash)


    if mongo.user.find({"email": email }).count() == 0:
        # mongo.new_user("email")
        x = mongo.user.insert_one(
            { 'email': email, 'passwords': [send], 'secrets': [] },
        )
    else:
        myquery = { "email": email }
        newvalues = { "$push": { "passwords": send } }
        mongo.user.update_one(myquery, newvalues)

    payload = {
        "email":email,
        "picture":picture,
        "alg":alg,
        "password":password,
        "encrypted":send,
        "hash":hash,
    }
    return payload

@app.get("/aes/{data}/{key}")
def aes_e(data: str, key: str):
    data = url_parse(data)
    key = url_parse(key)
    ciph = AESCipher(key)
    send = ciph.encrypt(data)
    
    myquery = { "email": "" }
    newvalues = { "$set": { "address": "Canyon 123" } }

    mongo.user.update_one(myquery, newvalues)
    payload = {
        "data":send
    }
    return payload


@app.get("/aes/encrypt/{data}")
def aes_encrypt(data: str):
    data = url_parse(data)
    key = "1234"
    ciph = AESCipher(key)
    send = ciph.encrypt(data)
    payload = {
        "data":send
    }
    return payload

@app.get("/aes/decrypt/{data}")
def aes_decrypt(data: str):
    key = "1234"
    ciph = AESCipher(key)
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