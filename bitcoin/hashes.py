import hashlib


def sha256(data):
    data = str(data).encode('utf-8')
    return hashlib.sha256(data) #return bytes


def ripemd160(data):
    ripemd160 = hashlib.new('ripemd160')
    data = str(data).encode('utf-8')
    ripemd160.update(data)
    return ripemd160.digest() #return bytes
