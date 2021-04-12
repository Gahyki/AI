class Player:
    def __init__(self, total_tokens, nb_taken_tokens, ls_taken_tokens, depth):
        self.total_tokens: int = total_tokens
        self.nb_taken_tokens: int = nb_taken_tokens
        self.ls_taken_tokens: [] = ls_taken_tokens
        # Even numbered depth will mean the play is Max
        self.depth: int = depth


def minmax(position, depth, alpha, beta):
    if depth == 0:
        return position
    if depth % 2 == 0:
        maxEval = float("-inf")
        for child in position:
            childEval = minmax(child, depth - 1, alpha, beta)
            maxEval = max(alpha, childEval)
            alpha = max(alpha, childEval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float("inf")
        for child in position:
            childEval = minmax(child, depth - 1, alpha, beta)
            minEval = min(minEval, childEval)
            beta = min(beta, childEval)
            if beta <= alpha:
                break
        return minEval
