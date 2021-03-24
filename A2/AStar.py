import math
import time
import numpy


def createhash(arr):
    hashtable = {}
    size = len(arr)
    for i in range(size):
        for j in range(size):
            hashtable[arr[i][j]] = (i, j)
    return hashtable, size


def creatematrix(hashtable, size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for v, i, j in hashtable.items():
        matrix[i][j] = v
    return matrix


def heuristics1(current, goal, values, size):
    # both matrices
    hsum = 0
    for v in values:
        # Regular Manhattan Distance
        hsum += abs(goal[v][0] - current[v][0]) + abs(goal[v][1] - current[v][1])
    return hsum


def heuristics2(current, goal, values, size):
    # both matrices
    hsum = 0
    for v in values:
        # Manhattan Distance For Matrix
        hsum += min(abs(goal[v][0] - current[v][0]), size - 1 - abs(goal[v][0] - current[v][0])) \
                + min(abs(goal[v][1] - current[v][1]), size - 1 - abs(goal[v][1] - current[v][1]))
    return hsum


def gdist(startx: int, starty: int, endx: int, endy: int):
    a = endx - startx
    b = endy - starty
    return a + b



# Step 1 - Create hashtables to make searching faster for current and goal
# Step 2 - Create heuristic based on hashtable