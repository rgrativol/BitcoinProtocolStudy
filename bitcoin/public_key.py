from ecdsa import VerifyingKey
from bitcoin.network import Network
from bitcoin.utils import *


class PublicKey:
    _version_byte = 0  # https://en.bitcoin.it/wiki/Base58Check_encoding

    def __init__(self, verifying_key: VerifyingKey):
        self._ecdsa_public_key = verifying_key

    def to_int(self):
        return int(self.to_bin(), 2)

    def to_bin(self):
        return b'\x04' + self._ecdsa_public_key.to_string()

    def address(self, network=Network.MAIN, compressed=False):
        network_version_byte = b'\x00'
        if network == Network.TEST:
            network_version_byte = b'\x6F '
        # 1 - Take the corresponding public key generated with it
        #  (65 bytes, 1 byte 0x04, 32 bytes corresponding to X coordinate, 32 bytes corresponding to Y coordinate)

        # 2 - Perform RIPEMD-160 hashing on the result of SHA-256
        data = hashes.ripemd160(hashes.sha256(self.to_bin()))

        # 3 - Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
        data = network_version_byte + data

        # 5 - Base58Check encoding (for better human readability)
        address = bytes_to_base58check(data)

        return address

    def to_hex(self):
        return b'04' + bin_to_hex(self._ecdsa_public_key.to_string())
