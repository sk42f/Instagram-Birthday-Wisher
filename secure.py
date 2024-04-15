from cryptography.fernet import Fernet
from base64 import b64encode
#Generate a strong key from fernet and store below
key = "strong feret key"
# we will be encrypting the below string.


# generate a key for encryption and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key

#key = Fernet.generate_key()

#pc.copy(key)

# Instance the Fernet class with the key
def encrypt(data):
	fernet = Fernet(key)
	encMessage = fernet.encrypt(data.encode())
	return encMessage


# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
def decrypt(data):
	fernet = Fernet(key)
	decMessage = fernet.decrypt(data).decode()
	return decMessage
