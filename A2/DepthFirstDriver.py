from DepthFirst import *
import time

f = open("puzzles.txt", "r")
results = open("outputDepth.txt",'w')
counter = 0

for line in f:
    start = eval(line)
    solution = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    puzzle = Puzzle(start)
    puzzle.depthFirstSearch(puzzle,solution)

