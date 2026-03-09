from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
 
def generate_key():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key,public_key

keshu_private_key,keshu_public_key = generate_key()
karan_private_key,karan_public_key = generate_key()

shared_key_1 = keshu_private_key.exchange(ec.ECDH(),karan_public_key)

secret_key_1 = HKDF(algorithm=hashes.SHA256(),length=32,salt=None,info=b'handshake data').derive(shared_key_1)

aesgcm = AESGCM(secret_key_1)
nonce = os.urandom(12)

message = b'hiii iam keshu'

label = "my secret"

ciphertext = aesgcm.encrypt(nonce,message,label.encode())
print("Ciphertext:",ciphertext)

shared_key_2 = karan_private_key.exchange(ec.ECDH(),keshu_public_key)

secret_key_2 = HKDF(algorithm=hashes.SHA256(),length=32,salt=None,info=b'handshake data').derive(shared_key_2)

aesgcm_2 = AESGCM(secret_key_2)

normaltext = aesgcm_2.decrypt(nonce,ciphertext,label.encode())
print("Normaltext:",normaltext)
print("normaltext:",normaltext.decode())

print(secret_key_1 == secret_key_2)
