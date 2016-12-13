# problemUrl- https://www.hackerrank.com/challenges/kruskalmstrsub
# Node class for storing rank, representative of set and the parent of the node
class Node:
    def __init__(self,value):
        self.parent = self
        self.representative = value
        self.rank = 0


class disjointSet:
    def __init__(self):
        self.setS = {}  # initialize empty dict for storing node

    def makeSet(self,vertexValue):  # function to initializing a node and add it to graph dictionary
        node = Node(vertexValue)
        self.setS[vertexValue]=node

    def findParent(self,node):  # function to find the parent of node
        if node.parent!=node:
            node.parent = self.findParent(node.parent)   # used for recursion and path compression
        return node.parent
    def printRepresent(self,vertex):    # function to return the representative of the set
        return self.findParent(self.setS[vertex]).representative

    def unionSet(self,vertex1,vertex2):  # function to do the union of two sets
        node1 = self.setS[vertex1]
        node2 = self.setS[vertex2]
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1==parent2:
            return
        if parent1.rank<parent2.rank:
            parent1.parent = parent2
        elif parent1.rank>parent2.rank:
            parent2.parent = parent1
        else:
            parent1.parent = parent2
            parent2.rank +=1




ds = disjointSet()

# edges.append([(0,1),4])
# edges.append([(1,2),8])
# edges.append([(2,3),7])
# edges.append([(3,4),9])
# edges.append([(4,5),10])
# edges.append([(5,6),2])
# edges.append([(0,1),4])
# edges.append([(7,6),1])
# edges.append([(0,7),8])
#
# edges.append([(5,3),14])

n,e = map(int,raw_input().strip().split(" "))
# for i in xrange(1,n+1):
#     ds.makeSet(i)
edges = []
for x in range(e):
    startVertex,endVertex,weight = map(int,raw_input().strip().split(" "))
    edges.append([(startVertex,endVertex),weight])

edges.sort(key=lambda x:x[0][0]+x[0][1]+x[1])
edges.sort(key=lambda x:x[1])




#print edges
finalEdges = []

ds = disjointSet()
for i in xrange(1,n+1):
    ds.makeSet(i)
totalWeight = 0
for edge in edges:
    startVertex,endVertex = edge[0]
    if startVertex not in ds.setS:
        ds.makeSet(startVertex)
    if endVertex not in ds.setS:
        ds.makeSet(endVertex)
    if ds.findParent(ds.setS[startVertex])==ds.findParent(ds.setS[endVertex]):
        pass
    else:
        ds.unionSet(startVertex,endVertex)
        finalEdges.append(edge)
        totalWeight += edge[1]
        if len(finalEdges)==n-1:
            break

print totalWeight
# for edge in finalEdges:
#     print edge
