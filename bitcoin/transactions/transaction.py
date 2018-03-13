class Transaction:
    version = 1  # v2? https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki

    def __init__(self):
        self.tx_in_count = 0  # Number of Transaction inputs (never zero)
        self.inputs = []  # A list of 1 or more transaction inputs or sources for coins
        self.tx_out_count = 0  # Number of Transaction outputs
        self.outputs = []  # A list of 1 or more transaction outputs or destinations for coins
        self.tx_witness = []  # A list of witnesses, one for each input; omitted if flag is omitted above
        self.lock_time = 0  # The block number or timestamp at which this transaction is unlocked (not used!)

    def add_input(self, tx_in):
        """
        Add a TxIn to the inputs
        :param tx_in: Transaction Input
        """
        self.inputs.append(tx_in)

    def add_output(self, tx_out):
        """
         Add a TxOut to the inputs
        :param tx_out: Transaction Output
        """
        self.outputs.append(tx_out)

    def total_output(self) -> float:
        """
        Total of output in BTC
        :return: Total BTC
        :rtype: float
        """
        return sum(self.outputs)

    def hash(self) -> str:
        """
        The transaction´s hash
        :return:  Hash
        :rtype: str
        """
        raise NotImplemented()
