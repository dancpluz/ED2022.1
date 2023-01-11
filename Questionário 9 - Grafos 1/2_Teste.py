class Graph():
    def __init__(self,vertices):
        self.graph = {}
        self.V = vertices
  
    def addEdge(self,f,t):
        
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.graph[u].append(v)
  
    def isCyclicUtil(self, v, visited, recStack):
  
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
  
        # The node needs to be popped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

n = int(input())
g = Graph(n)
for _ in range(n):
    entrada = input().split()
    for i in range(int(entrada[1])):
        g.addEdge(entrada[0], i)

if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")