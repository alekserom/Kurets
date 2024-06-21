import random
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def encrypt(raw):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    raw = pad(raw)
    iv = get_random_bytes(BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(raw.encode()))

def decrypt(enc):
    BS = AES.block_size
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    iv = enc[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[BS:]))

def isascii(s):
    try: 
        return len(s) != len(s.decode())
    except: UnicodeDecodeError
    
key = random.randint(100,999).to_bytes(16)

plain_text = "Hello world!"

cypher_text = encrypt(plain_text)

print (base64.b64encode(cypher_text))

for brut in range(100,999):
    key = brut.to_bytes(16)
    test = decrypt(cypher_text)
    if test.isascii() and len(test) > 3:
        print (test)
