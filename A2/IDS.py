import copy
import random
import time


class Node:
    state: []
    parent: None
    depth: None
    f_score: None

    def __init__(self, state, parent, depth, f_score):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.f_score = f_score

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getFscore(self):
        return self.f_score

    def setFscore(self, f_score):
        self.f_score = f_score


    def solPath(self):
        solPath = []
        depth = self.depth
        currNode = self

        while (depth != -1):
            solPath.append(currNode)
            currNode = currNode.parent
            depth = depth - 1

        solPath.reverse()
        return solPath


class Timer:
    def __init__(self):
        self.startTime = None

    def start(self):
        self.startTime = time.perf_counter()

    def getTime(self):
        passedTime = time.perf_counter() - self.startTime
        return passedTime

    def stop(self):
        passedTime = time.perf_counter() - self.startTime
        self.startTime = None
        print(f"Elapsed time: {passedTime:0.9f} seconds")

    def maxTime(self):
        self.startTime = None
        print(f"No Solution found")

def main():
    val = '((1; 2; 6); (8; 7; 3); (4; 5; 9))'
    listOfInputs = getList(parse_input(val))

    node = Node(listOfInputs, [], 0, 0)
    IDS(node)


def IDS(start_node):
    solNode = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    open_stack = []
    closed_stack = []
    maxDepth = 0
    iterDepth = 11
    t = Timer()
    t.start()

    open_stack.append(start_node)

    for i in range(iterDepth):
        while (len(open_stack) > 0):

            if t.getTime() >= 60: #set limit to 60 before outputting 'No solution'
                t.maxTime()
                return False, 0, 0, 0, 0

            if len(closed_stack) == 0:
                currNode = open_stack.pop()
                closed_stack.append(currNode)
            else:
                closed_stack.append(currNode)
                currNode = open_stack.pop()

            if (currNode.state == solNode): #comparing to goal state
                print("-  -  -  -  -  -  -  -  -  -")
                print("Parent State: " + str(currNode.parent.state))
                print("Solution State: " + str(currNode.state))
                print("Iteration Depth: " + str(i))
                print("-  -  -  -  -  -  -  -  -  -")
                solPath(currNode)
                searchPath(closed_stack)
                passedTime = t.getTime()
                t.stop()
                return True, passedTime, len(closed_stack), currNode.depth + 1, len(closed_stack)

            while (currNode.depth < maxDepth):
                if t.getTime() >= 60:
                    t.maxTime()
                    return False, 0, 0, 0, 0

                if (currNode.state == solNode):
                    print("-  -  -  -  -  -  -  -  -  -")
                    print("Parent State: " + str(currNode.parent.state))
                    print("State Reached: " + str(currNode.state))
                    print("Iteration Depth: " + str(i))
                    print("-  -  -  -  -  -  -  -  -  -")
                    solPath(currNode)
                    searchPath(closed_stack)
                    passedTime = t.getTime()
                    t.stop()
                    return True, passedTime, len(closed_stack), currNode.depth + 1, len(closed_stack)

                children = Children(currNode)

                for state in children:
                    if t.getTime() >= 60: #set limit to 60 before outputting 'No solution'
                        t.maxTime()
                        return False, 0, 0, 0, 0
                    if currNode.depth == 0:
                        open_stack.append(state)
                    elif not inStack(state.state, closed_stack):
                        open_stack.append(state)

                closed_stack.append(currNode)

                if (len(open_stack) == 0):
                    break
                else:
                    currNode = open_stack.pop()

                if (currNode.state == solNode):
                    print("-  -  -  -  -  -  -  -  -  -")
                    print("Parent State: " + str(currNode.parent.state))
                    print("Solution State Reached: " + str(currNode.state))
                    print("Iteration Depth: " + str(i))
                    print("-  -  -  -  -  -  -  -  -  -")
                    solPath(currNode)
                    searchPath(closed_stack)
                    passedTime = t.getTime()
                    t.stop()
                    return True, passedTime, len(closed_stack), currNode.depth+1, len(closed_stack)

        open_stack.clear()
        closed_stack.clear()
        maxDepth += 1
        open_stack.append(start_node)


def solPath(node):
    new_file = open("outputs/sol_path.txt", "w+")
    dimension = len(node.state)
    solution_path = node.solPath()
    ctr = 0

    for state in solution_path:
        while (ctr < dimension):
            new_file.write(str(state.state[ctr]) + "\n")
            ctr += 1

        new_file.write("\n")
        ctr = 0


def searchPath(closed_stack):
    new_file = open("outputs/search_path.txt", "w+")
    dimension = len(closed_stack[0].state)
    ctr = 0

    for i in reversed(closed_stack):
        while (ctr < dimension):
            new_file.write(str(i.state[ctr]) + "\n")
            ctr += 1

        new_file.write("\n")
        ctr = 0


def inStack(state, stack):
    for i in range(len(stack)):
        if state == stack[i].state:
            return True
    return False

def parse_input(inputStr):
    inputStr = eval(inputStr.replace(';', ','))
    return inputStr

def getList(tup):
    return list(map(getList, tup)) if isinstance(tup, (list, tuple)) else tup

def getIndex(listOfInputs, num):
    for sub_list in listOfInputs:
        if num in sub_list:
            return (listOfInputs.index(sub_list), sub_list.index(num))
    raise ValueError("'{num}' is not in list".format(num=num))


######movements along board######
def Left(listOfInputs, currIndex):
    list_copy = copy.deepcopy(listOfInputs)
    num_temp = list_copy[currIndex[0]][currIndex[1] + 1]
    list_copy[currIndex[0]][currIndex[1] +
                            1] = list_copy[currIndex[0]][currIndex[1]]
    list_copy[currIndex[0]][currIndex[1]] = num_temp
    return list_copy


def Right(listOfInputs, currIndex):
    list_copy = copy.deepcopy(listOfInputs)
    num_temp = list_copy[currIndex[0]][currIndex[1] - 1]
    list_copy[currIndex[0]][currIndex[1] -
                            1] = list_copy[currIndex[0]][currIndex[1]]
    list_copy[currIndex[0]][currIndex[1]] = num_temp
    return list_copy


def Up(listOfInputs, currIndex):
    list_copy = copy.deepcopy(listOfInputs)
    num_temp = list_copy[currIndex[0] - 1][currIndex[1]]
    list_copy[currIndex[0] - 1][currIndex[1]
    ] = list_copy[currIndex[0]][currIndex[1]]
    list_copy[currIndex[0]][currIndex[1]] = num_temp
    return list_copy


def Down(listOfInputs, currIndex):
    list_copy = copy.deepcopy(listOfInputs)
    num_temp = list_copy[currIndex[0] + 1][currIndex[1]]
    list_copy[currIndex[0] + 1][currIndex[1]
    ] = list_copy[currIndex[0]][currIndex[1]]
    list_copy[currIndex[0]][currIndex[1]] = num_temp
    return list_copy



def moveLeft(currIndex, dimension):
    if (currIndex[1] == dimension - 1):
        return False
    else:
        return True


def moveRight(currIndex):
    if (currIndex[1] == 0):
        return False
    else:
        return True


def moveUp(current_index):
    if (current_index[0] == 0):
        return False
    else:
        return True


def moveDown(current_index, dimension):
    if (current_index[0] == dimension - 1):
        return False
    else:
        return True

def Nodes(states_list, parent_node):
    nodes = []
    for state in states_list:
        node = Node(state, parent_node, parent_node.depth + 1, 0)
        nodes.append(node)

    return nodes

def Children(parent_node):
    listOfInputs = parent_node.state
    possible_moves = []
    dimension = len(listOfInputs)
    for row in listOfInputs:
        for j in row:
            index = getIndex(listOfInputs, j)
            if (moveLeft(index, dimension)):
                move = Left(listOfInputs, index)
                if move not in possible_moves:
                    possible_moves.append(move)
            if (moveRight(index)):
                move = Right(listOfInputs, index)
                if move not in possible_moves:
                    possible_moves.append(move)
            if (moveUp(index)):
                move = Up(listOfInputs, index)
                if move not in possible_moves:
                    possible_moves.append(move)
            if (moveDown(index, dimension)):
                move = Down(listOfInputs, index)
                if move not in possible_moves:
                    possible_moves.append(move)

    nodes = Nodes(possible_moves, parent_node)
    random.shuffle(nodes)
    return nodes



if __name__ == '__main__':
    main()
