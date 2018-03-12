from bitcoin.private_key import PrivateKey


def main():
    #private_key = PrivateKey('')
    import hashlib
    x = hashlib.sha256(b'bla').hexdigest()
    print(x)


if __name__ == '__main__':
    main()
