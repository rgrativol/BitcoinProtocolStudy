import hashlib


def sha256(data: bytes) -> bytes:
    """
    Perform the SHA-256 (Secure Hash Algorithm 2)
    :param data: Bytes to hash
    :return: SHA256 Hash
    :rtype: bytes
    """
    return hashlib.sha256(data).digest()


def ripemd160(data: bytes) -> bytes:
    """
    Perform the RIPEMD-160 (RACE Integrity Primitives Evaluation Message Digest) cryptographic hash 
    :param data: Bytes to hash
    :return: RIPEMD160 Hash
    :rtype: bytes
    """
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(data)
    return ripemd160.digest()
