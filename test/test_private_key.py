import unittest
from bitcoin.private_key import PrivateKey
import bitcoin.formatters as formatter


class TestPrivateKey(unittest.TestCase):
    def __init__(self, test_name):
        super(TestPrivateKey, self).__init__(test_name)
        # Use -> https://www.bitaddress.org/
        self.pk_hex = '5E2E2F133CB1457E54E28032A01ABD32450852ECC597867007BC721F65AEDF1A'  # 256bits
        self.pk_int = int(self.pk_hex, 16)  # Too big to write here..
        self.pk_wif = '5JXmHyq7SKrjr16dMaDtooWVnW1jC9fLYh9z9ZbGvrgrVQvR583'
        self.private_key_int = PrivateKey(self.pk_int)
        self.private_key_hex = PrivateKey(self.pk_hex)
        self.private_key_wif = PrivateKey(self.pk_wif)

    def test_private_key_to_int(self):
        self.assertEqual(self.private_key_int.to_int(), self.pk_int)
        self.assertEqual(self.private_key_hex.to_int(), self.pk_int)
        self.assertEqual(self.private_key_wif.to_int(), self.pk_int)

    def test_private_key_to_bin(self):
        pk_256_bits = formatter.int_to_256bits(self.pk_int)
        self.assertEqual(self.private_key_int.to_bin(), pk_256_bits)
        self.assertEqual(self.private_key_hex.to_bin(), pk_256_bits)
        self.assertEqual(self.private_key_wif.to_bin(), pk_256_bits)

    def test_private_key_to_wif(self):
        self.assertEqual(self.private_key_int.to_wif(), self.pk_wif)
        self.assertEqual(self.private_key_hex.to_wif(), self.pk_wif)
        self.assertEqual(self.private_key_wif.to_wif(), self.pk_wif)

    if __name__ == '__main__':
        unittest.main()
