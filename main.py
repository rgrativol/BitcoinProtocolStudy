from bitcoin import Network, PrivateKey


def main():
    private_key = PrivateKey('3781bb8845ed9006644f9bb89c35133de7d827cfbc4db60d83d95af80ff46cbe')
    public_key = private_key.public_key()

    print('Private Key: {0}\nPublic Key: {1}\nAddress: {2}'.format(private_key.to_hex(), public_key.to_hex(),
                                                                   public_key.address(network=Network.MAIN)))


if __name__ == '__main__':
    main()
