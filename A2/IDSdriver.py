from IDS import IDS
from IDS import Node


def main():
    list = inputgen()
    new_file = open("outputs/analysis.txt", "w+")
    noSol = 0
    execTime = 0
    totCost = 0
    solLength = 0
    searchLength = 0
    success = False

    for input in list:
        node = Node(input, [], 0, 0)
        success, tempTime, tempSearch, tempSol, tempCost = IDS(node)
        if success:
            execTime += tempTime
            searchLength += tempSearch
            solLength += tempSol
            totCost += tempCost
        else:
            noSol += 1

    analysis(noSol, execTime, totCost, solLength, searchLength, "Iterative-Deepening Search")

    noSol = 0
    execTime = 0
    totCost = 0
    solLength = 0
    searchLength = 0
    success = False



def inputgen():
    input_file = open("inputs/inputs.txt", "r")
    list_of_inputs = []

    for input in input_file:
        list_of_inputs.append(getList(parseInput(input)))

    return list_of_inputs


def analysis(noSol, execTime, totCost, solLength, searchLength, algo):
    new_file = open("outputs/analysis.txt", "a+")
    new_file.write("Algorithm: " + algo + "\n\n")
    new_file.write("Total Search Path: " + str(searchLength) + "\n")
    new_file.write("Average Search Path: " + str(searchLength / (20 - noSol)) + "\n")
    new_file.write("Total Solution Path: " + str(solLength) + "\n")
    new_file.write("Average Solution Path: " + str(solLength / (20 - noSol)) + "\n")
    new_file.write("Total 'No Solution': " + str(noSol) + "\n")
    new_file.write("Average 'No Solution': " + str(noSol / 20) + "\n")
    new_file.write("Total cost: " + str(totCost) + "\n")
    new_file.write("Average cost: " + str(totCost / (20 - noSol)) + "\n")
    new_file.write("Total execution time: " + str(execTime) + "s \n")
    new_file.write("Average execution time: " + str(execTime / (20 - noSol)) + "s \n")
    new_file.write("Total execution time with 'No Solution': " + str(execTime + noSol * 60) + "s \n")
    new_file.write("Average execution time with 'No Solution': " + str((execTime + noSol * 60) / (20)) + "s \n")


def parseInput(inputStr):
    inputStr = eval(inputStr.replace(';', ','))
    return inputStr


def getList(tup):
    return list(map(getList, tup)) if isinstance(tup, (list, tuple)) else tup


if __name__ == '__main__':
    main()
