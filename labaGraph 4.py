import networkx as nx
import matplotlib.pyplot as plt
import random
def matrixMultiplication(A, B):
    result = [[0]*len(A) for i in range(len(B[0]))]
    for row in range(len(A)):
        for column in range(len(A)):
            for i in range(len(B)):
                result[row][column]+=A[row][i]*B[i][column]
    return result

def xorMatrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > 0 or B[i][j] > 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
    return A
    
def andMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > 0 and A[j][i] > 0:
                A[i][j] = 1
                A[j][i] = 1
            else:
                A[i][j] = 0
                A[j][i] = 0
    return A

def getStraitMatrix(matrix):
    prevMatrix = matrix
    resMatrix = matrix
    for i in range(len(matrix)):
        prevMatrix = matrixMultiplication(prevMatrix, matrix)
        resMatrix = xorMatrix(resMatrix, prevMatrix)
    for i in range(len(resMatrix)):
        resMatrix[i][i]=1
    print("матрица достижимости")
    for i in resMatrix:
        print(i)
    return andMatrix(resMatrix)

def deleteNodeByIndex(nodes, index):
    pass

def deleteNode(nodes, node):
    pass

def printNezavComponents(connections, toDelete):
    for i in range(connections):
        if connections[i][0] == toDelete:
            whereElem = i
            break
    if len(connections[whereElem][1])==0:
        for i in range(whereElem+1, len(connections)):
            if len(connections[i][1])>0:
                printNezavComponents(connections, connections[i][0])
                return
        for i in connections:
            print(i[0], end=" ")
    #delete node
    tmp = connections.deepcopy()
    deleteNodeByIndex(tmp, where)
    printNezavComponents(tmp, connections[whereElem][0])
    #delete nodes
    tmp = connections.deepcopy()
    for i in connections[whereElem][1]:
        deleteNode(tmp, i)
    if len(connections) > whereElem+2:
        printNezavComponents(tmp, connections[whereElem+1])
    else:
        for i in tmp:
            print(i[0], end=" ")

n = int(input("Введите количество вершин графа "))
connections = [[i+1, list(map(int, input().split(" ")))] for i in range(n)]
printNezavComponents(connections, 1)

