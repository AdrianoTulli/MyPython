import os
import pytest
from Crypto.PublicKey import RSA
from project import AES_encrypt, RSA_encrypt, RSA_keys, hashing

@pytest.fixture
def test_f():
    return 'input_test.txt'

def test_AES(test_f):
    name, ext = os.path.splitext(test_f)
    k = b'0'*32
    AES_encrypt(test_f, k, name)
    f_enc = f"{name}.enc"

    assert os.path.exists(f_enc)
    os.remove(f_enc)

def test_RSA(test_f):
    RSA_keys()
    name, ext = os.path.splitext(test_f)
    with open('public.pem', 'rb') as pub_k:
        pub_key = RSA.import_key(pub_k.read())

    RSA_encrypt(test_f, pub_key, name)
    enc_file = f"{name}.enc"

    assert os.path.exists(enc_file)
    os.remove(enc_file)
    os.remove('private.pem')
    os.remove('public.pem')

def test_hashing(test_f):

    name, ext = os.path.splitext(test_f)
    k = b'0'*32

    AES_encrypt(test_f, k, name)
    enc_file = f"{name}.enc"

    hashing(enc_file, name)
    hash_f = f"{name}.hash"

    assert os.path.exists(hash_f)
    os.remove(enc_file)
    os.remove(hash_f)

if __name__ == '__main__':
    pytest.main()
