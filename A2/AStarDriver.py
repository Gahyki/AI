from AStar import *
# import multiprocessing
# import time
# from threading import Timer, Thread
#
#
# def check_timeout(status):
#     thread = Thread(target=astar, name="A*", args=(puzzle))
#     t = Timer(60, astar)
#     t.start()
#     thread.start()


# start = ((6, 1, 2), (7, 8, 3), (5, 4, 9))
start = ((5, 1, 2, 4),(9, 6, 3, 7),(13, 10, 16, 8),(14, 15, 11, 12))

puzzle = Puzzle(start)
solution, search = astar(puzzle)

print("-------------------------- Solution -----------------------------")
for p in solution:
    print(p)
print(len(solution))
print("-------------------------- Search -----------------------------")
for s in search:
    print(s)
print(len(search))
