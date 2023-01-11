class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def edgeDelete(self,vert):
        del self.connectedTo[vert]

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            return
        if t not in self.vertList:
            return
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    
    def removeEdge(self,f,t):
        if f not in self.vertList:
            return
        if t not in self.vertList:
            return
        for i in self.vertList[f].connectedTo:
            if i.id == t:
                self.vertList[f].edgeDelete(i)
                return

    def removeVertex(self,key):
        if key in self.vertList:
            self.numVertices = self.numVertices - 1
            del self.vertList[key]

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

n = int(input())
grafo = Graph()

for _ in range(n):
    entrada = input().split()
    if entrada[0] == 'IV':
        grafo.addVertex(entrada[1])
    elif entrada[0] == 'IA':
        grafo.addEdge(entrada[1], entrada[2], float(entrada[3]))
    elif entrada[0] == 'RV':
        grafo.removeVertex(entrada[1])
    elif entrada[0] == 'RA':
        grafo.removeEdge(entrada[1], entrada[2])

soma = 0
soma2 = 0
for i in grafo.vertList.values():
    soma += len(i.connectedTo.values())
    for p in i.connectedTo.values():
        soma2 += p

print(f'{grafo.numVertices} vertice(s), {soma} aresta(s) e peso total {soma2:.2f}.')