import networkx as nx
import matplotlib.pyplot as plt
import random
def matrixMultiplication(A, B):
    result = [[0]*len(A)]*len(B[0])
    for row in range(len(A)):
        for column in range(len(A)):
            for i in range(len(B)):
                result[row][column]+=A[row][i]*B[i][column]
    return result

def transpose(matrix):
    matrix = matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
    return matrix

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

G = nx.DiGraph()
n = int(input("Введите количество вершин графа "))
print("Введите матрицу смежности:")
matrixPrev = [list(map(int, input().split(" "))) for i in range(n)]
matrixStrait = getStraitMatrix([copyRow[:] for copyRow in matrixPrev])
print("матрица S")
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
print("Матрица смежности сильных компонент")
matrix = [[0]*len(straitComponents) for i in range(len(straitComponents))]
for i in range(n):
    for j in range(n):
        if(matrixPrev[i][j] == 1):
            startComponent = 0;
            endComponent = 0;
            while (i not in straitComponents[startComponent]):
                startComponent+=1
            while (j not in straitComponents[endComponent]):
                endComponent+=1
            matrix[startComponent][endComponent] = 1
for i in range(len(matrix)):
    matrix[i][i]=0


for i in matrix:
    print(i)
for row in range(len(matrix)):
    for column in range(len(matrix)):
        if(matrix[row][column]==1):
            G.add_edge(row, column)
plt.title("Концентрация графа")
nx.draw(G, with_labels=True, node_size = 200, node_color = 'purple', font_color = 'black')
plt.show()