class OutPoint:
    def __init__(self, tx_out_hash, tx_out_index):
        self.tx_out_hash = tx_out_hash
        self.tx_out_index = tx_out_index
