import unittest
from bitcoin.private_key import PrivateKey
from bitcoin.public_key import PublicKey
import bitcoin.formatters as formatter


class TestPublicKey(unittest.TestCase):
    def __init__(self, test_name):
        super(TestPublicKey, self).__init__(test_name)
        private_key = PrivateKey('0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D')

        self.public_key_hex = '04D0DE0AAEAEFAD02B8BDC8A01A1B8B11C696BD3D66A2C5F10780D95B7DF42645' \
                              'CD85228A6FB29940E858E7E55842AE2BD115D1ED7CC0E82D934E929C97648CB0A'.lower()

        self.public_key = private_key.public_key()

    def test_to_hex(self):
        self.assertEqual(self.public_key.to_hex(), self.public_key_hex.encode())  # encode returns bytes

    def test_to_bin(self):
        self.assertEqual(self.public_key.to_bin(), formatter.hex_to_bin(self.public_key_hex))

    def test_to_address(self):
        self.assertEqual(self.public_key.address(), '1GAehh7TsJAHuUAeKZcXf5CnwuGuGgyX2S')


if __name__ == '__main__':
    unittest.main()
