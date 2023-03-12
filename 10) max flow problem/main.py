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
    def __init__(self, start_vertex, end_vertex, capacity, isResidual = False):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.isResidual = isResidual
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity

    def __str__(self):
        return self.start_vertex.key + "->" + self.end_vertex.key + ": " + str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)


class ListGraph:
    def __init__(self):
        self.lst = []
        self.dict_graph = {}
        self.dictionary = {}
        self.edges_list = []
        self.graph = []

    def insertVertex(self, vertex):
        if vertex.key in self.lst:
            pass
        else:
            self.lst.append(vertex.key)
            self.dictionary[vertex.key] = len(self.lst) - 1
            self.dict_graph[vertex.key] = []

    def insertEdge(self, vertex1, vertex2, capacity, isResidual = False):
        if vertex1.key in self.lst and vertex2.key in self.lst:
            edg_1 = (vertex1.key, vertex2.key, isResidual, capacity)
            if edg_1 not in self.edges_list:
                self.edges_list.append((vertex1.key, vertex2.key, isResidual, capacity))
                self.dict_graph[vertex1.key].append(Edge(vertex1, vertex2, capacity, isResidual))
                self.graph.append(Edge(vertex1, vertex2, capacity, isResidual))
            else:
                pass
        else:
            pass

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
            print("{0} : [".format(key), end="")
            for i in values:
                print("({0}, {1}, {2}, {3}, {4}) ".format(i.end_vertex.key, i.capacity, i.flow, i.residual, i.isResidual), end="")
            print(']')
        return string


def bfs(graph: ListGraph, start_vertex):
    parent = [-1 for i in range(len(graph.lst))]
    visited = [0 for i in range(len(graph.lst))]
    queue = [graph.getVertexIdx(start_vertex)]
    visited[queue[0]] = 1
    while queue:
        elem = queue.pop(0)
        neigh = graph.neighbours(elem)
        for i in neigh:
            if visited[graph.getVertexIdx(i.end_vertex.key)] == 0 and i.residual > 0 and not i.isResidual:
                queue.append(graph.getVertexIdx(i.end_vertex.key))
                visited[graph.getVertexIdx(i.end_vertex.key)] = 1
                parent[graph.getVertexIdx(i.end_vertex.key)] = elem
    return parent


def path_analyse(graph, start_vertex, end_vertex, parent):
    act_vertex_index = graph.getVertexIdx(end_vertex)
    min_capacity = np.inf
    if parent[act_vertex_index] == -1:
        return 0
    else:
        while act_vertex_index != graph.getVertexIdx(start_vertex):
            for idx, el in enumerate(graph.dict_graph[graph.getVertex(parent[act_vertex_index])]):
                if el.end_vertex.key == graph.getVertex(act_vertex_index) and not el.isResidual:
                    if el.residual < min_capacity:
                        min_capacity = el.residual
            act_vertex_index = parent[act_vertex_index]
    return min_capacity


def augmentation(graph, start_vertex, end_vertex, parent, min_capacity):
    act_vertex_index = graph.getVertexIdx(end_vertex)
    while act_vertex_index != graph.getVertexIdx(start_vertex):
        for idx, el in enumerate(graph.dict_graph[graph.getVertex(parent[act_vertex_index])]):
            if el.end_vertex.key == graph.getVertex(act_vertex_index):
                if not el.isResidual:
                    el.flow += min_capacity
                    el.residual -= min_capacity
                elif el.isResidual:
                    el.residual += min_capacity
        act_vertex_index = parent[act_vertex_index]
    return min_capacity


def ford_fulkerson(graph: ListGraph):
    parent = bfs(graph, 's')
    minimum = path_analyse(graph, 's', 't', parent)
    sum_of_flow = minimum
    while minimum > 0:
        augmentation(graph, 's', 't', parent, minimum)
        parent = bfs(graph, 's')
        minimum = path_analyse(graph, 's', 't', parent)
        sum_of_flow += minimum
    print(sum_of_flow)
    printGraph(graph)


def printGraph(g):
    n = g.getOrder()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for j in nbrs:
            print(j, end=";  ")
        print()
    print("-------------------")
    print("")


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    lst = [graf_0, graf_1, graf_2, graf_3]

    for graph in lst:
        A = ListGraph()
        for i in graph:
            A.insertVertex(Node(i[0]))
            A.insertVertex(Node(i[1]))
        for i in graph:
            A.insertEdge(Node(i[0]), Node(i[1]), i[2])
            A.insertEdge(Node(i[0]), Node(i[1]), i[2], True)
        ford_fulkerson(A)


if __name__ == "__main__":
    main()
