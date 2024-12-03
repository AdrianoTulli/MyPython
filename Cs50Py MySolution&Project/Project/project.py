from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import hashlib
import os

def AES_encrypt(file_p, key, name):

    with open(file_p, 'rb') as to_read:
        text = to_read.read()

    c = AES.new(key, AES.MODE_CBC)
    ct = c.encrypt(pad(text, AES.block_size))

    temp_f = name + '.enc'

    with open(temp_f, 'wb') as file_enc:
        file_enc.write(c.iv)
        file_enc.write(ct)

    print(f'Crypted file created:{name}.enc')
    return

def RSA_encrypt(file_p, pk, name):

    with open(file_p, 'rb') as to_read:
        text = to_read.read()
    c = PKCS1_OAEP.new(pk)
    ct = c.encrypt(text)

    temp_f = name + '.enc'
    with open(temp_f, 'wb') as file_enc:
        file_enc.write(ct)
    print(f'Crypted file generated: {name}.enc ')
    return

def RSA_keys():

    key = RSA.generate(2048)
    key_prv = key.export_key()
    key_pub = key.publickey().export_key()

    with open('private.pem', 'wb') as file_prv:
        file_prv.write(key_prv)

    with open('public.pem', 'wb') as file_pub:
        file_pub.write(key_pub)
    print('RSA key generated.')

    return

def hashing(file_p, name):

    with open(file_p, 'rb') as file:
        data = file.read()

    hash_object = hashlib.sha3_256(data)
    hash_digest = hash_object.hexdigest()

    temp_f = name + '.hash'

    with open(temp_f, 'w') as hash_f:
        hash_f.write(hash_digest)

    print(f'Hash SHA-3 generated: {name}.hash')
    return

if __name__ == '__main__':
    file_p = input('File path: ').strip()
    name = os.path.basename(file_p)
    name, ext = os.path.splitext(name)

    if not os.path.exists(file_p):
        print(f'File {file_p} not found')
        exit()
    metod = input('Choose between AES and RSA (AES/RSA): ').strip().upper()

    if metod not in ['AES', 'RSA']:
        print('Invalid option.')
        exit()

    elif metod == 'AES':
        key = get_random_bytes(32)
        AES_encrypt(file_p, key, name)

    elif metod == 'RSA':
        if not os.path.exists('public.pem') or not os.path.exists('private.pem'):
            RSA_keys()
        with open('public.pem', 'rb') as pp:
            pk = RSA.import_key(pp.read())
            RSA_encrypt(file_p, pk, name)

    hashing(file_p, name)
