from ecdsa import SigningKey, SECP256k1
from secrets import randbits
import bitcoin.formatters as formatter
from bitcoin.public_key import PublicKey


class PrivateKey():
    _curve = SECP256k1

    def __init__(self, private_key=None):

        if not private_key:
            # If no private key is provided then creates one
            self._secret_exponent = self._generate_secret_exponent()

        elif formatter.is_int(private_key):
            # Creates from integer number
            self._secret_exponent = private_key

        elif formatter.is_256bit_hex_string(private_key):
            # Creates from hex number
            self._secret_exponent = int(private_key, 16)

        elif formatter.is_wif_pk(private_key):
            self._secret_exponent = formatter.base58check_to_int(private_key)

        if not self._secret_exponent: raise ValueError('Please check the private key value provided.')

        self._ecdsa_private_key = SigningKey.from_secret_exponent(secexp=self._secret_exponent, curve=self._curve)

    def to_256bits(self):
        """
        The Private Key in bytes
        :return: 
        :rtype: bytes
        """
        return self._ecdsa_private_key.to_string()

    def to_wif(self, main_net=True):
        """
        Private Key Wallet Import Format  
        :return: WIF string
        :rtype: str
        """
        # Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses.
        # Also add a 0x01 byte at the end if the private key will correspond to a compressed public key
        if main_net:
            data = b'80' + self.to_hex()
        else:
            data = b'ef' + self.to_hex()
        return formatter.bin_to_wif(data)  # https://en.bitcoin.it/wiki/Wallet_import_format

    def to_hex(self):
        """
        Private Key in Hexadecimal Format (64 characters [0-9A-F])
        :return: Hexadecimal number
        :rtype: bytes
        """
        return formatter.bin_to_hex(self.to_256bits())

    def to_base64(self):
        """
        The Private Key in Base64 encoding (44 characters)
        :return: Base64 string
        :rtype: str
        """
        raise NotImplemented()

    def to_int(self):
        return self._secret_exponent

    def get_public_key(self):
        return PublicKey(self._ecdsa_private_key.get_verifying_key())

    def _generate_secret_exponent(self):
        while True:
            # random 256bits number
            random_int = int(randbits(256), 16)
            # curve order n denotes the number of points on the curve
            if 1 <= random_int < self._curve.order:
                break
        return random_int
