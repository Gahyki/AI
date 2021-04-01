from DepthFirst import *
import time

f = open("puzzles.txt", "r")
results = open("outputDepth.txt",'w')

for line in f:
    start = eval(line)
    solution = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    puzzle = Puzzle(start)
    puzzle.depthFirstSearch(puzzle,solution)


