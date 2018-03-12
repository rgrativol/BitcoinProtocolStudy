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

    def test_private_key_to_int(self):
        self.assertEqual(PrivateKey(self.pk_int).to_int(), self.pk_int)
        self.assertEqual(PrivateKey(self.pk_hex).to_int(), self.pk_int)
        self.assertEqual(PrivateKey(self.pk_wif).to_int(), self.pk_int)

    def test_private_key_to_bin(self):
        pk_bin = formatter.int_to_256bit(self.pk_int)
        private_key = PrivateKey(self.pk_int)
        self.assertEqual(private_key.to_bin(), pk_bin)

    def test_private_key_to_wif(self):
        pass


if __name__ == '__main__':
    unittest.main()
