class PNT:
    def __init__(self, total_tokens):
        self.total_tokens: int = total_tokens
        self.ls_tokens: [] = [i+1 for i in range(self.total_tokens)]

