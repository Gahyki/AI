import heapq


# Graph of nodes and options to take
class Puzzle:
    def __init__(self, matrix):
        # current state of puzzle, xy location of each value
        if type(matrix) is list:
            self.puzzle = matrix
        else:
            self.puzzle = self.__matrixtopuzzle(matrix)
        self.size = len(matrix)
        self.heuristic = self.heuristics2()

    def __matrixtopuzzle(self, matrix):
        # puzzle list has each element of matrix in a single dimension form
        length = len(matrix)
        puzzle = []

        for i in range(length):
            for j in range(length):
                puzzle.append(matrix[i][j])
        return puzzle

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

    def heuristics1(self):
        hsum = 0
        # Change to hamming distance
        # Regular Hamming distance
        for i, v in enumerate(self.puzzle):
            if v != 1 and v != i + 1:
                hsum += 1
        return hsum

    def heuristics2(self):
        hsum = 0
        # Manhattan Distance For Matrix
        for i, v in enumerate(self.puzzle):
            # Get starting position
            sx = i // self.size
            sy = i % self.size

            # Get ending position
            ex = (v - 1) // self.size
            ey = (v - 1) % self.size
            # hsum += abs(ex - sx) + abs(ey - sy)
            hsum += min(abs(ex - sx), self.size - 1 - abs(ex - sx)) \
                + min(abs(ey - sy), self.size - 1 - abs(ey - sy))
        return hsum

    def solved(self):
        return self.heuristic == 0

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

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __le__(self, other):
        return self.heuristic <= other.heuristic

class OpenList:
    # Min Priority Queue
    def __init__(self):
        # List of all potential elements
        self.elements = []

    def put(self, heuristic_value, potential):
        # Pushed into queue using heap
        heapq.heappush(self.elements, (heuristic_value, potential))

    def get(self):
        # returns only the potential element
        # the heuristic value is not returned
        return heapq.heappop(self.elements)

    def isempty(self):
        return not self.elements

    def checkinside(self, option):
        # Method to check if neighbor is inside the MinPQ
        for _, puzzle in self.elements:
            if puzzle == option:
                return True
        return False

def cost(puzzle):
    hsum = 0
    # Change to hamming distance
    # Regular Hamming distance
    for i, v in enumerate(puzzle):
        if v != i + 1:
            hsum += 1
    return hsum


def astar(puzzle):
    # List of different possibilities
    openlist = OpenList()
    openlist.put(0, puzzle)

    # Solution path
    closelist = []

    # Dictionary containing state of matrix in string form to find avoid repetition of actions
    uniquecloselist = {}

    # Cost of each possibility
    costlist = {}
    # Initializing cost list
    costlist[str(puzzle.puzzle)] = 0

    # List of considered possibilities
    searchlist = []

    # Main loop
    while not openlist.isempty():
        # Current node to explore
        current = openlist.get()

        # Removing possibilities from past traversals
        openlist.elements = []

        # Adding to closelists
        closelist.append(current[1])
        uniquecloselist[str(current[1].puzzle)] = None

        # Compare with the goal
        if current[1].solved():
            break
        else:
            # Getting each neighbor and its heuristic value
            for option in current[1].neighbors():
                new_cost = costlist[str(current[1].puzzle)] + cost(option.puzzle)
                if str(option.puzzle) not in uniquecloselist.keys() or new_cost < costlist[str(option.puzzle)]:
                    fscore = new_cost + option.heuristic
                    costlist[str(option.puzzle)] = new_cost
                    openlist.put(fscore, option)
                    searchlist.append(option)
    return closelist, searchlist
