class TxOut:
    def __init__(self):
        self.value = 0.0
        self.pk_script_length = ''
        self.pk_script = ''

    def serialize(self):
        raise NotImplemented()