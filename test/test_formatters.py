import unittest
from bitcoin.utils import *


class TestFormatters(unittest.TestCase):
    def test_hex_to_int(self):
        self.assertEqual(hex_to_int('f'), 15)
        self.assertRaises(ValueError, hex_to_int, 'g')

    def test_int_to_hex(self):
        self.assertEqual(int_to_hex(15), 'f')
        self.assertRaises(ValueError, int_to_hex, '10')

    def test_bin_to_hex(self):
        self.assertEqual(bin_to_hex(b'\xff'), b'ff')
        self.assertRaises(ValueError, bin_to_hex, 'ff')

    def test_hex_to_bin(self):
        self.assertEqual(hex_to_bin('ff'), b'\xff')
        self.assertRaises(ValueError, hex_to_bin, b'\xff')

    def test_is_int(self):
        self.assertTrue(is_int(1))
        self.assertFalse(is_int(1.1))

    def test_is_256bit_hex_string(self):
        self.assertTrue(
            is_256bit_hex_string('5E2E2F133CB1457E54E28032A01ABD32450852ECC597867007BC721F65AEDF1A'))
        self.assertFalse(is_256bit_hex_string('FF'))

    def test_base58check_to_int(self):
        base58check = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
        int_value = int('0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D', 16)
        self.assertEqual(base58check_to_int(base58check), int_value)

    def test_bin_to_wif(self):
        data = '800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
        self.assertEqual(bin_to_wif(data), '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')


if __name__ == '__main__':
    unittest.main()
