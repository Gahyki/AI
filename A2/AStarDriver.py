from AStar import *
import time



print("-------------------------- A* Algorithm -----------------------------")
# Initializing total variables for stats
nb_tests = 20
SOT_counter = 0
SET_counter = 0
NST_counter = 0
T_cost = 0
T_time = 0


# Opening input text file
f = open("puzzles.txt", "r")
for line in f:
    start = eval(line)

    puzzle = Puzzle(start)
    a_solution, a_search, a_cost, a_time = astar(puzzle)

    SOT_counter += len(a_solution)
    SET_counter += len(a_search)
    for p in a_solution:
        if p == "no solution":
            NST_counter += 1
    T_cost += a_cost
    T_time += a_time


# Initializing averages variables for stats
SOA_counter = SOT_counter / nb_tests
SEA_counter = SET_counter / nb_tests
NSA_counter = NST_counter / nb_tests
A_cost = T_cost / nb_tests
A_time = T_time / nb_tests


# Output
print("Total length of solution path: " + str(SOT_counter))
print("Average length of solution path: " + str(SOA_counter))

print("Total length of search path: " + str(SET_counter))
print("Average length of search path: " + str(SEA_counter))

print("Total number of no solution: " + str(NST_counter))
print("Average number of no solution: " + str(NSA_counter))

print("Total cost: " + str(T_cost))
print("Average cost: " + str(A_cost))

print("Total execution time: " + str(T_time) + " seconds")
print("Average execution time: " + str(A_time) + " seconds")
