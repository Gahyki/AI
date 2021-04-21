import math

class Node:
    def __init__(self, parent, maxPlayer, allToken, listOfTakenToken, depthNode, childList,
                 pnt):
        self.parent = parent
        self.maxPlayer = maxPlayer
        self.allToken = allToken
        self.listOfTakenToken = listOfTakenToken
        self.depthNode = depthNode
        self.childList = childList
        self.pnt = pnt


def getmultiples(checkNumber, numberToCompare):
    if checkNumber == 1:
        return True

    if (checkNumber % numberToCompare == 0) or (numberToCompare % checkNumber == 0):
        return True
    else:
        return False


def prime(number):
    if number > 1:
        if number > 1:
            for i in range(1, int(number // 2)+1):
                if (number % i) == 0:
                    return False
                    break
                else:
                    return True
        else:
            return False
    return False


def string(inputStr):
    array_of_values = inputStr.split();

    allToken = int(array_of_values.pop(0))

    number_of_taken_tokens = int(array_of_values.pop(0))

    list_of_taken_tokens = []
    if number_of_taken_tokens != 0:
        index = 0
        while index < number_of_taken_tokens:
            list_of_taken_tokens.append(int(array_of_values.pop(0)))
            index = index + 1

    depth = int(array_of_values.pop(0))

    return allToken, number_of_taken_tokens, list_of_taken_tokens, depth


def legalMoves(allToken, takenTokenNum, listofTakenToken):
    if takenTokenNum == 0:
        range_of_numbers = list(range(1, (int)(allToken / 2 + 1)))
        possible_choices = [num for num in range_of_numbers if num % 2 == 1]
    else:
        last_move = listofTakenToken[-1]
        possible_choices = []
        for num in list(range(1, allToken + 1)):
            if num not in listofTakenToken and getmultiples(num, last_move):
                possible_choices.append(num)

    return possible_choices


def rootNode(allToken, listofTakenToken, takenTokenNum):
    depthNode = 0

    if takenTokenNum == 0 or takenTokenNum % 2 == 0:
        maxPlayerParent = True
    else:
        maxPlayerParent = False

    treeRoot = Node(None, maxPlayerParent, allToken, listofTakenToken, depthNode, [], None)

    treeRootChilder = addChildren(treeRoot, len(treeRoot.listOfTakenToken), treeRoot.allToken,
                                         treeRoot.listOfTakenToken)

    return treeRootChilder


def addChildren(parentNode, takenTokenNum, allToken, listofTakenToken):
    move = legalMoves(allToken, takenTokenNum, listofTakenToken)

    if len(move) > 0:
        depthNode = parentNode.depthNode + 1
        maxPlayerParent = not parentNode.maxPlayer

        for move in move:

            newMove = []
            for m in listofTakenToken:
                newMove.append(m)

            newMove.append(move)

            childNode = Node(parentNode, maxPlayerParent, allToken, newMove, depthNode,
                             [], move)
            parentNode.childList.append(childNode)

    return parentNode

def abAlgo(node, depth, alpha, beta, maxPlayer, nodeVisited, nodeEvaluated, maxDepth,
           brachingChildern):
    if node.parent is not None:
        childnode = addChildren(node, len(node.listOfTakenToken), node.allToken,
                                                     node.listOfTakenToken)
    else:
        childnode = node
        if depth == 0:
            depth = node.allToken
    if depth == 0 or len(childnode.childList) == 0:
        nodeEvaluated = nodeEvaluated + 1

        if childnode.depthNode > maxDepth:
            maxDepth = childnode.depthNode

        eN = gameBoard(childnode)
        return eN, childnode.pnt, nodeVisited, nodeEvaluated, maxDepth, brachingChildern
    if maxPlayer:
        value = -math.inf # math infini

        brachingChildern = brachingChildern + len(childnode.childList)
        for child in childnode.childList:
            nodeVisited = nodeVisited + 1

            if child.depthNode > maxDepth:
                maxDepth = child.depthNode
            valueEval, move, nodeVisited, nodeEvaluated, maxDepth, brachingChildern = abAlgo(
                child, depth - 1, alpha, beta, False, nodeVisited, nodeEvaluated, maxDepth,
                brachingChildern)
            value = max(value, valueEval)
            alpha = max(alpha, value)

            if beta <= alpha:
                break

            if value == valueEval:
                if child.pnt < move:
                    move = child.pnt

        return value, move, nodeVisited, nodeEvaluated, maxDepth, brachingChildern

    else:
        value = math.inf

        brachingChildern = brachingChildern + len(childnode.childList)

        for child in childnode.childList:
            nodeVisited = nodeVisited + 1

            if child.depthNode > maxDepth:
                maxDepth = child.depthNode

            valueEval, move, nodeVisited, nodeEvaluated, maxDepth, brachingChildern =abAlgo (
                child, depth - 1, alpha, beta, True, nodeVisited, nodeEvaluated, maxDepth,
                brachingChildern)

            value = min(value, valueEval)
            beta = min(beta, value)

            if alpha >= beta:
                break
            if value == valueEval:
                if child.pnt < move:
                    move = child.pnt

        return value, move, nodeVisited, nodeEvaluated, maxDepth, brachingChildern


def gameBoard(node): # 2.5 static board evalution

    if len(node.childList) == 0:
        if node.maxPlayer:
            return -1.0
        else:
            return 1.0
    lastchange = node.listOfTakenToken[-1]

    multiples = 1
    if node.maxPlayer == False:
        multiples = -1

    if 1 not in node.listOfTakenToken:
        return 0

    if lastchange == 1:
        if len(node.childList) % 2 == 0:
            return multiples * -0.5
        else:
            return multiples * 0.5

    if prime(lastchange):
        count = 0

        for child in node.childList:
            if getmultiples(child.pnt, lastchange):
                count = count + 1

        if count % 2 == 0:
            return multiples * -0.7
        else:
            return multiples * 0.7

    else:
        search = node.allToken

        while search > 0:
            if prime(search):
                if getmultiples(lastchange, search):
                    break;
                else:
                    search = search - 1
            else:
                search = search - 1

        count = 0
        if search != 0:
            for child in node.childList:
                if child is not node.listOfTakenToken:
                    if getmultiples(child.pnt, search):
                        count = count + 1

        if count % 2 == 0:
            return multiples * -0.6
        else:
            return multiples * 0.6
