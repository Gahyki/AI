import A3Game
import math
from time import perf_counter

listOfTestCases = []
inputs = open("test.txt", "r")
new_file = open("output.txt", "w")

for inputString in inputs:
    tokens = inputString.partition("TakeTokens")[0]
    listOfTestCases.append(tokens)

count = 1
for inputString in listOfTestCases:

    inputString = inputString.rstrip()

    new_file.write("\n\nTest Case: " + str(count))
    new_file.write("\n"+inputString)
    count += 1

    allToken, tokenNumber, listOfTakenToken, depth = A3Game.string(
        inputString)

    root = A3Game.rootNode(allToken, listOfTakenToken, tokenNumber)

    nodeVisited = 1
    nodeEvaluated = 0
    maxDepth = 0
    branching_factor_total_children = 1

    timerStart = perf_counter()
    value, move_to_do, nodeVisited, nodeEvaluated, maxDepth, branching_factor_total_children = A3Game.abAlgo(
        root, depth, -math.inf, math.inf, True, nodeVisited, nodeEvaluated,
        maxDepth, branching_factor_total_children)
    TimerEnd = perf_counter()

    execution_time = TimerEnd - timerStart

    if branching_factor_total_children == 0:
        branching_factor = 0
    else:
        branching_factor = round((nodeVisited / branching_factor_total_children), 1)

    # print output
    new_file.write("\nsolution")
    new_file.write("\nMove: " + str(move_to_do))
    new_file.write("\nValue: " + str(value))
    new_file.write("\nNumber of Nodes Visited: " + str(nodeVisited))
    new_file.write("\nNumber of Nodes Evaluated: " + str(nodeEvaluated))
    new_file.write("\nMax Depth Reached: " + str(maxDepth))
    new_file.write("\nAvg Effective Branching Factor: " + str(branching_factor))
    new_file.write("\nExecution Time: " + str(execution_time) + "secs" + "\n")