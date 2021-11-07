from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def rsa_encrypt(plain_text, key):
	public_key = key.publickey().exportKey('PEM')
	message = str.encode(plain_text)

	rsa_public_key = RSA.importKey(public_key)
	rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
	encrypted_text = rsa_public_key.encrypt(message)
	b64encrypted_text = base64.b64encode(encrypted_text)

	return b64encrypted_text


def rsa_decrypt(encrypted, key):
	private_key = key.export_key('PEM')

	encrypted = base64.b64decode(encrypted)
	rsa_private_key = RSA.importKey(private_key)
	rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
	decrypted_text = rsa_private_key.decrypt(encrypted).decode()

	return decrypted_text