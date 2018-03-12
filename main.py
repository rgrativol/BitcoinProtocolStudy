from bitcoin.private_key import PrivateKey


def main():
    # private_key = PrivateKey('')

    import base58
    import bitcoin.formatters as formatter
    a = formatter.unhexlify('800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D')
    x = base58.b58encode_check(a)

    print(x)


if __name__ == '__main__':
    main()
