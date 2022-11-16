import networkx as nx
import matplotlib.pyplot as plt
import random

def colorSort(array, graph):
	graph.sort(array)
	return getColorArray(array)

def getColorArray(matrix):
    colors = []
    for i in range(len(matrix)):
        colors.append(0)
    color = 0
    for i in range(len(matrix)):
        if colors[i] == 0:
            color += 1
            colors[i] = color
        else:
            continue
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                colors[j] = color
                for k in range(len(matrix)):
                    if matrix[j][k] == 1:
                        matrix[i][k] = 1
    return colors

G=nx.DiGraph()
n = int(input("Введите количество вершин графа "))
matrix = []
connections = []
for i in range(n):
    matrix.append([0 for i in range(n)])
    connections.append(list(map(int, input("C какими вершинами соединена вершина "+str(i+1)+" ").split(" "))))
    for j in connections[i]:
        matrix[i][int(j)-1] = 1

for i in range(len(connections)):
    for j in connections[i]:
        G.add_edge(i+1, j)

if input("выберите способ (1/2)") == "1":
	colorArray = getColorArray(matrix)
else:
	colorArray = colorSort(matrix, G)

nx.draw_circular(G, with_labels=True, node_size = 200, node_color=colorArray)
plt.show()