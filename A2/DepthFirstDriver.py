from DepthFirst import *
import time

f = open("puzzles.txt", "r")
results = open("outputDepth.txt",'a')
start_time = time.time()
for line in f:
    start = eval(line)
    solution = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    puzzle = Puzzle(start)
    puzzle.depthFirstSearch(puzzle,solution)

print("total running time " + str(start_time))
print("average running time" + str(start_time/20))

