from PIL import Image
import requests
import hashlib



def get_img(url):
	res = requests.get(url, stream=True)
	img = Image.open(res.raw)
	return img.getdata()

def arr_to_str(x):
	str = b''
	for p in x:
		str += p[0].to_bytes(1, byteorder='big') + p[1].to_bytes(1, byteorder='big') + p[2].to_bytes(1, byteorder='big')
	return str

def hash_img_url(url):
	img = get_img(url)
	bin = arr_to_str(img)
	hash = hashlib.sha256(bin).hexdigest()
	return hash