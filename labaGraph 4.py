import copy

sets = []

def deleteNodeByIndex(nodes, index):
	for i in nodes[index][1]:
		try:
			nodes[findElem(nodes, i)][1].remove(nodes[index][0])
		except:
			pass
	nodes.pop(index)

def findElem(connections, element):
	for i in range(len(connections)):
		if connections[i][0] == element:
			return i
	return -1

def printNezavComponents(connections, toDelete):
	if connections == []:
		return
	whereElem = findElem(connections, toDelete)
	if len(connections[whereElem][1])==0:
		for i in range(whereElem+1, len(connections)):
			if len(connections[i][1])>0:
				printNezavComponents(connections, connections[i][0])
				return
		s1 = set()
		for i in connections:
			s1.add(i[0])
		sets.append(s1)
	#delete node
	tmp = copy.deepcopy(connections)
	deleteNodeByIndex(tmp, whereElem)
	printNezavComponents(tmp, connections[whereElem][0])
	#delete nodes
	tmp = copy.deepcopy(connections)
	for i in connections[whereElem][1]:
		deleteNodeByIndex(tmp, findElem(tmp, i))
	if len(connections) > whereElem+2:
		printNezavComponents(tmp, connections[whereElem+1][0])
	else:
		s1 = set()
		for i in tmp:
			s1.add(i[0])
		sets.append(s1)

n = int(input("Введите количество вершин графа "))
connections = [[i+1, list(map(int, input().split(" ")))] for i in range(n)]
printNezavComponents(connections, 1)
for i in sets:
	for j in sets:
		if(i.issubset(j) and not i==j):
			try:
				sets.remove(i)
			except:
				pass

i = 0
while (i<len(sets)):
	j = i+1
	while (j<len(sets)):
		if sets[i] == sets[j]:
			sets.pop(j)
		else:
			j+=1
	i+=1

for i in sets:
	print(i)

