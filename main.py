from bitcoin.private_key import PrivateKey


def main():
    private_key = PrivateKey('3781bb8845ed9006644f9bb89c35133de7d827cfbc4db60d83d95af80ff46cbe')
    public_key = private_key.public_key()


if __name__ == '__main__':
    main()
