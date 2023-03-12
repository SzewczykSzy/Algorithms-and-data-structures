import graf_mst
import numpy as np


class Node:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, start_vertex, end_vertex, value=None):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.value = value


class ListGraph:
    def __init__(self):
        self.lst = []
        self.dict_graph = {}
        self.dictionary = {}
        self.edges_list = []

    def insertVertex(self, vertex):
        if vertex.key in self.lst:
            pass
        else:
            self.lst.append(vertex.key)
            self.dictionary[vertex.key] = len(self.lst) - 1
            self.dict_graph[vertex.key] = []

    def insertEdge(self, vertex1, vertex2, value):
        if vertex1.key in self.lst and vertex2.key in self.lst:
            edg_1 = (vertex1.key, vertex2.key, value)
            edg_2 = (vertex2.key, vertex1.key, value)
            if edg_1 not in self.edges_list and edg_2 not in self.edges_list:
                self.edges_list.append((vertex1.key, vertex2.key, value))
                self.edges_list.append((vertex2.key, vertex1.key, value))
                self.dict_graph[vertex1.key].append((vertex2.key, value))
                self.dict_graph[vertex2.key].append((vertex1.key, value))
            else:
                pass
        else:
            pass

    def deleteVertex(self, vertex):
        if vertex.key in self.lst:
            idx = self.dictionary[vertex.key]
            self.lst.pop(idx)
            self.dictionary.pop(vertex.key)
            temp = 0
            for el in self.dictionary.items():
                self.dictionary[el[0]] = temp
                temp += 1
            temp_lst = self.dict_graph[vertex.key]
            del self.dict_graph[vertex.key]
            for key in self.dict_graph.keys():
                for i in temp_lst:
                    if key == i[0]:
                        self.dict_graph[key].remove((vertex.key, i[1]))
        else:
            pass

    def deleteEdge(self, vertex1, vertex2):
        if vertex1.key in self.lst and vertex2.key in self.lst:
            for i in self.edges_list:
                if i[0] == vertex1.key and i[1] == vertex2.key:
                    self.dict_graph[vertex1.key].remove((vertex2.key, i[2]))
                    self.dict_graph[vertex2.key].remove((vertex1.key, i[2]))
                    self.edges_list.remove((i[0], i[1], i[2]))
                    self.edges_list.remove((i[1], i[0], i[2]))

    def getVertexIdx(self, vertex):
        return self.dictionary[vertex]

    def getVertex(self, vertex_idx):
        key_list = list(self.dictionary.keys())
        val_list = list(self.dictionary.values())
        position = val_list.index(vertex_idx)
        return key_list[position]

    def neighbours(self, vertex_idx):
        vertex = self.getVertex(vertex_idx)
        return self.dict_graph[vertex]

    def getOrder(self):
        return len(self.lst)

    def size(self):
        sum = 0
        for keys in self.dict_graph.values():
            for j in keys:
                sum += 1
        return sum//2

    def edges(self):
        lst = []
        for i in self.dict_graph.keys():
            for j in self.dict_graph[i]:
                lst.append((i, j))
        return lst

    def __str__(self):
        string = ""
        for key, values in self.dict_graph.items():
            print("{0} : {1}".format(key, values), end="")
            print()
        return string


def prime_algorithm(graph: ListGraph, start_vertex):
    size = graph.getOrder()
    intree = [0 for i in range(size)]
    distance = [np.inf for i in range(size)]
    parent = [-1 for i in range(size)]
    MST = ListGraph()
    sum = 0
    for i in graph.dict_graph.keys():
        MST.insertVertex(Node(i))
    act_vertex = start_vertex
    while intree[graph.getVertexIdx(act_vertex)] == 0:
        intree[graph.getVertexIdx(act_vertex)] = 1
        for i in graph.dict_graph[act_vertex]:
            if i[1] < distance[graph.getVertexIdx(i[0])] and intree[graph.getVertexIdx(i[0])] == 0:
                distance[graph.getVertexIdx(i[0])] = i[1]
                parent[graph.getVertexIdx(i[0])] = graph.getVertexIdx(act_vertex)
        temp_2_min = np.inf
        for v in graph.lst:
            if intree[graph.getVertexIdx(v)] == 0 and distance[graph.getVertexIdx(v)] < temp_2_min:
                temp_2_min = distance[graph.getVertexIdx(v)]
                act_vertex = v
        if all(intree) == 1:
            return MST, sum
        sum += temp_2_min
        MST.insertEdge(Node(act_vertex), Node(graph.getVertex(parent[graph.getVertexIdx(act_vertex)])), temp_2_min)


def printGraph(g):
    n = g.getOrder()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(j, w, end=";")
        print()
    print("-------------------")


def main():
    graph = ListGraph()
    for i in range(len(graf_mst.graf)):
        graph.insertVertex(Node(graf_mst.graf[i][0]))
        graph.insertVertex(Node(graf_mst.graf[i][1]))
    for i in range(len(graf_mst.graf)):
        graph.insertEdge(Node(graf_mst.graf[i][0]), Node(graf_mst.graf[i][1]), graf_mst.graf[i][2])

    mst, sum = prime_algorithm(graph, 'A')

    printGraph(mst)


if __name__ == "__main__":
    main()
