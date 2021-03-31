from AStar import *
import time



start = ((6, 1, 2), (7, 8, 3), (5, 4, 9))
# start = ((1, 2,  3),(4, 6, 5),(7, 8, 9))
# start = ((1, 2, 3, 4, 5, 7, 14),(8, 9, 10, 11, 12, 13, 6),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),
#          (29, 30, 31, 32, 49, 33, 34),(36, 37, 38, 39, 40, 41, 35),(43, 44, 45, 46, 47, 48, 42))


print("-------------------------- A* Algorithm -----------------------------")
nb_tests = 20

SOT_counter = 0
SOA_counter = SOT_counter / nb_tests

SET_counter = 0
SEA_counter = SET_counter / nb_tests

NST_counter = 0
NSA_counter = NST_counter / nb_tests

T_cost = 0
A_cost = T_cost / nb_tests

T_time = 0
A_time = T_time / nb_tests

puzzle = Puzzle(start)
a_solution, a_search, a_cost, a_time = astar(puzzle)

SOT_counter += len(a_solution)
SET_counter += len(a_search)
for p in a_solution:
    if p == "no solution":
        NST_counter += 1
T_cost += a_cost
T_time += a_time


print("Total length of solution path" + str(SOT_counter))
print("Average length of solution path" + str(SOA_counter))

print("Total length of search path: " + str(SET_counter))
print("Average length of search path: " + str(SEA_counter))

print("Total number of no solution: " + str(NST_counter))
print("Average number of no solution: " + str(NSA_counter))

print("Total cost: " + str(T_cost))
print("Average cost: " + str(A_cost))

print("Total execution time: " + str(T_time) + " seconds")
print("Average execution time: " + str(A_time) + " seconds")
