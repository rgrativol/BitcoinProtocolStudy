from binascii import hexlify, unhexlify
import base58
import bitcoin.hashes as hashes


def hex_to_int(value) -> int:
    """
    Convert hexadecimal to decimal
    :param value: Hexadecimal number
    :return: Decimal number
    :rtype: int
    """
    try:
        return int(value, 16)
    except:
        raise ValueError("Value must be in hex format")


def int_to_hex(value) -> str:
    """
    Convert decimal to hexadecimal
    :param value: Decimal number
    :return: Hexadecimal number
    :rtype: str
    """
    try:
        return hex(value).rstrip('L').lstrip('0x')
    except:
        raise ValueError("Value must be in int format")


def bin_to_hex(data) -> bytes:
    """
    Convert bytes to hexadecimal
    :param data: Bytes to be converted
    :return: Hexadecimal number
    :rtype: bytes
    """
    if is_bin(data):
        return hexlify(data)
    else:
        raise ValueError("Data must be binary")


def hex_to_bin(data) -> bytes:
    """

    :param data: 
    :return: 
    """
    return unhexlify(data)


def bin_to_base58check(data):
    pass


def is_hex(value) -> bool:
    """
    Check if a value is a hexadecimal
    :param value: Hexadecimal number
    :return: True or False
    :rtype: bool
    """
    # make sure this is a string
    if not isinstance(value, str):
        return False
    # if there's a leading hex string indicator, strip it
    if value.startswith('0x'):
        value = value[2:]
    # try to cast the string as an int
    try:
        hex_to_int(value)
    except ValueError:
        return False
    else:
        return True


def is_int(value) -> bool:
    """
    Check if a number is int
    :param value: Integer number
    :return: True or False
    :rtype: bool
    """
    return isinstance(value, int)


def int_to_256bits(value, endianness='big'):
    if is_int(value):
        return value.to_bin(length=32, byteorder=endianness)
    else:
        raise ValueError('Value must be an int')


def is_256bit_hex_string(value) -> bool:
    """

    :param value: 
    :return: 
    """
    return isinstance(value, str) and len(value) == 64 and is_hex(value)


def is_wif_pk(value) -> bool:
    return 51 <= len(value) <= 52  # wif normal and compressed


def base58check_to_int(value) -> int:
    # Creates from WIF (Wallet Import Format) see: https://en.bitcoin.it/wiki/Wallet_import_format
    wifi_decoded_hex = bin_to_hex(base58.b58decode_check(value))[2:]  # Drops the network byte
    return int(wifi_decoded_hex, 16)

def bytes_to_base58check(data):
    return base58.b58encode_check(data)

def is_bin(data):
    return isinstance(data, (bytes, bytearray))


def bin_to_wif(data):
    # Wallet Import Format (WIF, also known as Wallet Export Format) is a way of encoding
    #  a private ECDSA key so as to make it easier to copy.
    return base58.b58encode_check(hex_to_bin(data))
