class Player:
    def __init__(self, total_tokens, nb_taken_tokens, ls_taken_tokens, depth):
        self.total_tokens: int = total_tokens
        self.nb_taken_tokens: int = nb_taken_tokens
        self.ls_taken_tokens: [] = ls_taken_tokens
        # Even numbered depth will mean the play is Max
        self.depth: int = depth
