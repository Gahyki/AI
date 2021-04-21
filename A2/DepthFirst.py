import time
from itertools import chain
class Puzzle():
    def __init__(self, matrix):
        # current state of puzzle, xy location of each value
        if type(matrix) is list:
            self.puzzle = matrix
        else:
            self.puzzle = self.__matrixtopuzzle(matrix)
        self.size = len(matrix)

    def __matrixtopuzzle(self, matrix):
        # puzzle list has each element of matrix in a single dimension form
        length = len(matrix)
        puzzle = []

        for i in range(length):
            for j in range(length):
                puzzle.append(matrix[i][j])
        return puzzle
    def __str__(self):
        # matrix output in a string form
        matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        # index/value
        for i, v in enumerate(self.puzzle):
            x = i // self.size
            y = i % self.size
            matrix[x][y] = v
        output = "\n--- Puzzle Output ---\n"
        for row in matrix:
            output += str(row) + "\n"
        output += "--- Puzzle Output ---\n"
        return str(output)

    def neighbors(self):
        # All nodes connected to this node
        unique = {}
        result = []

        # Combination x and y (numbers that could be applied)
        cx = [1, -1, 0, 0]
        cy = [0, 0, 1, -1]

        # Generate all possibilities
        for i, v in enumerate(self.puzzle):
            # Get x and y coordinates of the chosen value
            oldx = i // self.size
            oldy = i % self.size
            for px, py in zip(cx, cy):
                # Get new x and y coordinates of the generated possibility
                newx = oldx + px
                newy = oldy + py
                if 0 <= newx < self.size and 0 <= newy < self.size:
                    temppuzzle = list(self.puzzle)
                    newindex = newx * self.size + newy
                    temppuzzle[oldx * self.size + oldy] = temppuzzle[newindex]
                    temppuzzle[newindex] = v
                    if str(temppuzzle) not in unique.keys():
                        unique[str(temppuzzle)] = v
                        obj = Puzzle(temppuzzle)
                        obj.size = self.size
                        result.append(obj)
        return result



    def depthFirstSearch(self,start,goal_state):
        queue = [start] # taking the first node as an element
        uniqueVisited = {} # set of node.
        uniqueQueue = {}
        visited = []
        goal = list(chain.from_iterable(goal_state))

        start_time = time.time()
        while queue:
            if(time.time() - start_time>60):
                print("out of time")
                print("no solution found in 60 sec")
                return False

            current_node = queue.pop(0)
           # print(current_node)
            visited.append(current_node)
            uniqueVisited[str(current_node.puzzle)] = None

            if(str(current_node.puzzle) == str(goal)):
                print("Solution found")
                print("number of visited node \n"+str(len(visited)))
                return True
            else:
                newChildren = current_node.neighbors()
                for i in range(len(newChildren)):
                    if str(newChildren[i].puzzle) not in uniqueVisited.keys() and str(newChildren[i].puzzle) not in uniqueQueue.keys():
                        queue.insert(0, newChildren[i])
                        uniqueQueue[str(newChildren[i].puzzle)] = None



