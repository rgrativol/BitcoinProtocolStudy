from ecdsa import VerifyingKey
import bitcoin.formatters as formatter


class PublicKey():
    _version_byte = 0  # https://en.bitcoin.it/wiki/Base58Check_encoding

    def __init__(self, verifying_key: VerifyingKey):
        self._ecdsa_public_key = verifying_key

    def to_int(self):
        pass
