from Crypto.Random import get_random_bytes
from pyDes import *

def des3_encrypt(plain_text, key):
	k = triple_des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
	return k.encrypt(plain_text)


def des3_decrypt(cipher, key):
	k = triple_des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
	return k.decrypt(cipher, padmode=PAD_PKCS5).decode()



key = get_random_bytes(24)
data = "hello worleda"

c = des3_encrypt(data, key)
print("key:", c)
print("original: ", des3_decrypt(c, key))