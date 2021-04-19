from A3Players import Player
from A3Game import PNT
import copy


def minmax(self, pnt, player, alpha, beta):
    if 7 in player.ls_taken_tokens:
        return pnt.remaining_tokens # to be replaced

    if pnt.depth % 2 == 0:
        maxEval = float("-inf")
        for child in pnt.neighbors():
            #Creating child game instance
            node = copy.deepcopy(pnt) # deep copy
            temp = copy.deepcopy(player) # deep copy
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



# Player(10, 3, 4, [2, 6], 4)
pnt = PNT(7)
a = copy.deepcopy(pnt)
# print(pnt.getmultiples(3))
# print(pnt.getfactors(3))
# print(pnt.neighbors())
a.all_tokens.remove(3)
print(a.all_tokens)
print(pnt.all_tokens)



# requires input file
file = open("./testcase.txt")
for i in file.readlines():
    if "TakeTokens" in i:
        raw_input = i.split()[1:]
        input_numbers = []
        temp = []
        for j in range(len(raw_input)):
            if j == (len(raw_input) - 1):
                input_numbers.append(temp)
                input_numbers.append(int(raw_input[j]))
            elif j < 2:
                input_numbers.append(int(raw_input[j]))
            else:
                temp.append(int(raw_input[j]))

        # Input numbers are done formatting here
        print(input_numbers)

# requires output file