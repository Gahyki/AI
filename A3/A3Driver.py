from A3Players import Player
from A3Game import PNT


def minmax(self, pnt, player, alpha, beta):
    if 7 in player.ls_taken_tokens:
        return pnt.remaining_tokens # to be replaced

    if player.depth % 2 == 0:
        maxEval = float("-inf")
        for child in pnt.neighbors():
            #Creating child game instance
            node = pnt # deep copy
            temp = player # deep copy
            temp.take(node, child)

            childEval = self.minmax(node, player.depth + 1, alpha, beta)
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


max = Player()
min = Player()
# Player(10, 3, 4, [2, 6], 4)
pnt = PNT(7)
print(pnt.all_tokens)
print(pnt.getmultiples(3))
print(pnt.getfactors(3))
print(pnt.neighbors())
minmax(max,)


# requires input file
# requires output file