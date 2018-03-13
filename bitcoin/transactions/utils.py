from bitcoin.formatters import is_hex, bin_to_hex, hex_to_bin


def count_bytes(hex_s) -> int:
    """
    Calculate the number of bytes of a given hex string.
    :param hex_s: Hexadecimal string
    :return: int
    :rtype: int
    """
    assert (is_hex(hex_s))
    return int(len(hex_s) / 2)


def flip_endian(s):
    """
    
    :param s: 
    :return: 
    """
    if is_hex:
        return bin_to_hex(hex_to_bin(s)[::-1])
    return s[::-1]
