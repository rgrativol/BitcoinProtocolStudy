from ecdsa import SigningKey, SECP256k1
from secrets import randbits
from bitcoin.network import Network
from bitcoin.public_key import PublicKey
from bitcoin.utils import *


class PrivateKey:
    _curve = SECP256k1  # secp256k1 refers to the parameters of the ECDSA curve used in Bitcoin

    def __init__(self, private_key=None):

        if not private_key:
            # If no private key is provided then creates one
            self._secret_exponent = self._generate_secret_exponent()

        elif is_int(private_key):
            # Creates from integer number
            self._secret_exponent = private_key

        elif is_256bit_hex_string(private_key):
            # Creates from hex number
            self._secret_exponent = int(private_key, 16)

        elif is_wif_pk(private_key):
            self._secret_exponent = base58check_to_int(private_key)

        if not self._secret_exponent: raise ValueError('Please check the private key value provided.')

        self._ecdsa_private_key = SigningKey.from_secret_exponent(secexp=self._secret_exponent, curve=self._curve)

    def to_bin(self) -> bytes:
        """
        The Private Key in bytes
        :return: 256bits key
        :rtype: bytes
        """
        return self._ecdsa_private_key.to_string()

    def to_wif(self, network=Network.MAIN) -> str:
        """
        Private Key Wallet Import Format  
        :return: WIF string
        :rtype: str
        """
        # Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses.
        # Also add a 0x01 byte at the end if the private key will correspond to a compressed public key
        if network == Network.MAIN:
            data = b'80' + self.to_hex()
        if network == Network.TEST:
            data = b'ef' + self.to_hex()
        return bin_to_wif(data)  # https://en.bitcoin.it/wiki/Wallet_import_format

    def to_hex(self) -> bytes:
        """
        Private Key in Hexadecimal Format (64 characters [0-9A-F])
        :return: Hexadecimal number
        :rtype: bytes
        """
        return bin_to_hex(self.to_bin())

    def to_base64(self) -> str:
        """
        The Private Key in Base64 encoding (44 characters)
        :return: Base64 string
        :rtype: str
        """
        raise NotImplemented()

    def to_int(self) -> int:
        """
         The Private Key integer number
         from 0x1 to 0xFFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFE BAAE DCE6 AF48 A03B BFD2 5E8C D036 4140
        :return: Private key integer 
        :rtype: int
        """
        return self._secret_exponent

    def public_key(self) -> PublicKey:
        """
        The Public Key related to this Private Key
        :return: PublicKey object
        :rtype: PublicKey
        """
        return PublicKey(self._ecdsa_private_key.get_verifying_key())

    def _generate_secret_exponent(self) -> int:
        """
        Generate random private key
        :return: 256bits number
        :rtype: int
        """
        while True:
            # random 256bits number
            random_int = int(randbits(256), 16)
            # curve order n denotes the number of points on the curve
            if 1 <= random_int < self._curve.order:
                break
        return random_int
