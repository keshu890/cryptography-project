from cryptography.hazmat.primitives.asymmetric import x25519, ed25519
from cryptography.hazmat.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def x25519_key_pair():
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def ed25519_key_pair():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_key(private_key, public_key0):
    shared_key = private_key.exchange(public_key0)
    return shared_key

def derive_key_material(shared_key):
    salt = os.urandom(16)
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=salt, info=b'handshake data')
    return hkdf.derive(shared_key)

def encrypt_file(hkdf, filename):
    with open(filename, 'rb') as f:
        data = f.read()
        aesgcm = AESGCM(hkdf)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce, ciphertext

def decrypt_file(hkdf, nonce, ciphertext, filename_output):
    aesgcm = AESGCM(hkdf)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    with open(filename_output, 'wb') as f:
        f.write(plaintext)

def signature(private_key, data):
    return private_key.sign(data)

def verification(public_key, data, signature):
    try:
        public_key.verify(signature,data)
        return True
    except:
        return False
    


