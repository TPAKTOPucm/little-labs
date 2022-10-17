import networkx as nx
import matplotlib.pyplot as plt
import random
n = int(input("Введите количество вершин графа "))
print(Введите матрицу смежности:)
matrixPrev = [[input().split(" ") for j in range(n)] for i in range(n)]
matrixStrait = [[input().split(" ") for j in range(n)] for i in range(n)]
#Вычёркиваем
straitComponents = []
used = []
for i in range(n):
    if i in used:
        continue
    straitComponents.append([])
    for j in range(n):
        if j in used:
            continue
        if(matrixStrait[i][j]=="1"):
            straitComponents[len(straitComponents)-1].append(j)
            used.append(j)
print("Сильные компоненты")
for i in straitComponents:
    print(i)

matrix = [[]*len(straitComponents)]
for i in range(n):
    for j in range(n):
        if(matrixPrev[i][j] == "")

for i in range(n)

for i in range(len(matrix)):
    print(matrix[i])
for row in range(len(matrix)):
    for column in range(len(matrix)):
        if(matrix[row][column]==1):
            G.add_edge(row+1, column+1)
plt.title("Граф, построенный на основе матрицы смежности")
nx.draw(G, with_labels=True, node_size = 200, node_color = 'purple', font_color = 'black')
plt.show()