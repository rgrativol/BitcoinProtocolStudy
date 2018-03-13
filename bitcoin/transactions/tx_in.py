class TxIn:
    def __init__(self, prev_outpoint, script_sig):
        self.prev_outpoint = prev_outpoint
        self.script_sig = script_sig
        """
        Since replacement is not used currently, all transactions Bitcoin creates have 
        LockTime = 0 and Sequence = UINT_MAX. This is the case with the genesis block's generation transaction.
        See: https://bitcoin.stackexchange.com/questions/2025/what-is-txins-sequence
        """
        self.sequence = 2 ** 32 - 1  # uint_max
