from linkedlist import LinkedList
from node import Node

class Graph:
    def __init__(self, n):
        self.vertexList = []
        self.edges = 0
        self.vertices = 0
        self.current = 1

        for _ in range(n):
            self.addVertex()

    def _getVertex(self, u):
        return self.vertexList[u-1]

    def addVertex(self):
        new_vertex = LinkedList()
        new_vertex.append(Node(self.current))
        self.vertexList.append(new_vertex)
        self.current += 1
        self.vertices += 1

    """ def removeVertex(self, name):
        find = 0
        i = 0
        j = 0
        while i < self.vertices and find == 0:
            if self.vertexList[i][0].data == name:
                self.vertexList.pop(i)
                self.vertices -= 1
                find = 1
            i += 1
        if find == 0:
            raise ValueError("O vértice {} não se encontra no grafo!".format(name))
        for i in range(self.vertices):
            if self.vertexList[i].index(name) != -1:
                self.vertexList[i].remove(name) """
    
    def _addEdgeAux(self, u, v):
        # currentVertex = self._getVertex(v)
        currentVertex = self._getVertex(u)
        currentVertex.append(v)

    def addEdge(self, u, v):
        self._addEdgeAux(u, v)
        self._addEdgeAux(v, u)
        self.edges += 1
    
    """ def _removeEdgeAux(self, u, v):
        currentVertex = self._getVertex(u)
        currentVertex.remove(v) """
        
    """ def removeEdge(self, u, v):
        self._removeEdgeAux(u, v)
        # self._removeEdgeAux(v, u)
        self.edges -= 1 """

    """ def connected(self, u, v):
        vertex = self._getVertex(u)
        if vertex.index(v) != -1:
            return True
        return False """
    
    def degree(self, u):
        vertex = self._getVertex(u)
        return len(vertex) - 1

    def __repr__(self):
        if self.vertices <= 0:
            return ""
        else:
            r = str(self.vertexList[0])
            for i in range(1,self.vertices):
                r += "\n" + str(self.vertexList[i])
            return r
    
    def __str__(self):
        return self.__repr__()