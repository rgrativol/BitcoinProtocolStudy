class TxIn:
    def __init__(self, previous_output, signature_script):
        self.previous_output = previous_output
        self.script_length = 0
        self.signature_script = signature_script  # scriptSig
        self.sequence = 2 ** 32 - 1  # UINT_MAX  https://bitcoin.stackexchange.com/questions/2025/what-is-txins-sequence


    def serialize(self):
        raise NotImplemented()
