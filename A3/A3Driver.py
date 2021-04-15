from A3Players import Player
from A3Game import PNT


def minmax(self, pnt, player, alpha, beta):
    if 7 in player.ls_taken_tokens:
        return pnt.remaining_tokens
    if player.depth % 2 == 0:
        maxEval = float("-inf")
        for child in pnt.neighbors:
            childEval = self.minmax(child, player.depth + 1, alpha, beta)
            maxEval = max(alpha, childEval)
            alpha = max(alpha, childEval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float("inf")
        for child in pnt.neighbors():
            childEval = self.minmax(child, player.depth + 1, alpha, beta)
            minEval = min(minEval, childEval)
            beta = min(beta, childEval)
            if beta <= alpha:
                break
        return minEval


# pnt = PNT(7)
# print(pnt.total_tokens)
# print(pnt.ls_tokens)


# requires input file
# requires output file