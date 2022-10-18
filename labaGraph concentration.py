import networkx as nx
import matplotlib.pyplot as plt
import random
def matrixMultiplication(A, B):
    result = []
    for row in range(len(A)):
        result.append([])
        for column in range(len(A)):
            result[row].append(0);
            for i in range(len(B)):
                result[row][column]+=A[row][i]*B[i][column]
    return result

def transpose(matrix):
    result = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result

def xorMatrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > 0 and B[i][j] > 0:
                A[i][j] = 1

def getStraitMatrix(matrix):
    prevMatrix = matrix
    resMatrix = matrix
    for i in range(len(matrix)):
        prevMatrix = matrixMultiplication(prevMatrix, matrix)
        resMatrix = xorMatrix(resMatrix, prevMatrix)
    for i in range(len(resMatrix)):
        resMatrix[i][i]=1
    return xorMatrix(resMatrix, transpose(resmMtrix))

n = int(input("Введите количество вершин графа "))
print("Введите матрицу смежности:")
matrixPrev = [list(map(int, input().split(" "))) for i in range(n)]
matrixStrait = getStraitMatrix(matrixPrev)
for i in matrixStrait:
    print(i)

straitComponents = []
used = []
for i in range(n):
    if i in used:
        continue
    straitComponents.append([])
    for j in range(n):
        if j in used:
            continue
        if(matrixStrait[i][j]==1):
            straitComponents[len(straitComponents)-1].append(j)
            used.append(j)
print("Сильные компоненты")
for i in straitComponents:
    print(i)

matrix = [[0]*len(straitComponents)]*len(straitComponents)
for i in range(n):
    for j in range(n):
        if(matrixPrev[i][j] == 1):
            startComponent = 0;
            endComponent = 0;
            while not(i in straitComponents[startComponent]):
                startComponent+=1
            while not(i in straitComponents[endComponent]):
                endComponent+=1
            matrix[startComponent][endComponent] = 1
for i in range(len(matrix)):
    matrix[i][i]=0


for i in matrix:
    print(i)
for row in range(len(matrix)):
    for column in range(len(matrix)):
        if(matrix[row][column]==1):
            G.add_edge(row+1, column+1)
plt.title("Граф, построенный на основе матрицы смежности")
nx.draw(G, with_labels=True, node_size = 200, node_color = 'purple', font_color = 'black')
plt.show()