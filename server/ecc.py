from ecc.curve import Curve25519
from ecc.key import gen_keypair
from ecc.cipher import ElGamal


(pri_key, pub_key) = gen_keypair(Curve25519)
plaintext = b"I am plaintext."



def ecc_encrypt(plain_text):
	cipher_elg = ElGamal(Curve25519)
	C1, C2 = cipher_elg.encrypt(plain_text, pub_key)
	print(C1)
	print(C2)

# def ecc_encrypt(pri_key):
# 	cipher_elg = ElGamal(Curve25519)
# 	new_plaintext = cipher_elg.decrypt(pri_key, C1, C2)

ecc_encrypt(plaintext)

from Crypto.PublicKey import ECC
key = ECC.generate(curve='P-256')
print(key)


# from Crypto.PublicKey import ECC

# key = ECC.generate(curve='P-256')

# f = open('myprivatekey.pem','wt')
# f.write(key.export_key(format='PEM'))
# f.close()

# f = open('myprivatekey.pem','rt')
# key = ECC.import_key(f.read())
# print(key)