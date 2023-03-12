import numpy as np
from copy import copy


class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    pass


class MatrixGraph:
    def __init__(self):
        self.lst = []
        self.graph = []
        self.dictionary = {}

    def insertVertex(self, vertex):
        vertex = Node(vertex)
        if vertex.key in self.lst:
            pass
        else:
            self.lst.append(vertex.key)
            self.graph.append([0])
            for i in range(len(self.lst)):
                for j in range(i):
                    if len(self.graph[i]) < len(self.lst):
                        self.graph[i].append(0)
            if len(self.lst) > len(self.graph[0]):
                self.graph[0].append(0)
            self.dictionary[vertex.key] = len(self.lst) - 1

    def insertEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1.key in self.lst and vertex2.key in self.lst:
            i = self.dictionary.get(vertex1.key)
            j = self.dictionary.get(vertex2.key)
            self.graph[i][j] = 1
            self.graph[j][i] = 1
        else:
            pass

    def deleteVertex(self, vertex):
        vertex = Node(vertex)
        if vertex.key in self.lst:
            idx = self.dictionary[vertex.key]
            self.lst.pop(idx)
            self.dictionary.pop(vertex.key)
            temp = 0
            for el in self.dictionary.items():
                self.dictionary[el[0]] = temp
                temp += 1
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    if j == idx:
                        self.graph[i].pop(idx)
            self.graph.pop(idx)
        else:
            pass

    def deleteEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1.key in self.lst and vertex2.key in self.lst:
            idx_1 = self.dictionary[vertex1.key]
            idx_2 = self.dictionary[vertex2.key]
            self.graph[idx_1][idx_2] = 0
            self.graph[idx_2][idx_1] = 0

    def getVertexIdx(self, vertex):
        vertex = Node(vertex)
        return self.dictionary[vertex.key]

    def getVertex(self, vertex_idx):
        key_list = list(self.dictionary.keys())
        val_list = list(self.dictionary.values())
        position = val_list.index(vertex_idx)
        return key_list[position]

    def neighbours(self, vertex_idx):
        neigh = []
        for i in range(len(self.graph)):
            if self.graph[vertex_idx][i] != 0:
                neigh.append(i)
        return neigh

    def order(self):
        return len(self.lst)

    def size(self):
        sum = 0
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    sum += 1
        return sum//2

    def edges(self):
        lst = []
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    lst.append((self.getVertex(i), self.getVertex(j)))
        return lst

    def toNumpy(self):
        return np.array(self.graph)

    def __str__(self):
        str = ""
        for row in self.graph:
            print("[", end="")
            for col in row:
                print(col, end=" ")
            print("]")
        return str


def ullman(used_cols, current_row, G, P, M, result=0, no_recursion=0):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.dot(M, G).T)):
            return result + 1, no_recursion
        else:
            return result, no_recursion
    for idx, el in enumerate(used_cols):
        if used_cols[idx] == 0:
            M[current_row][idx] = 1
            for i in range(len(M[0])):
                if i != idx:
                    M[current_row][i] = 0
            used_cols[idx] = 1
            result, no_recursion = ullman(used_cols, current_row + 1, G, P, M, result, no_recursion + 1)
            used_cols[idx] = 0
    return result, no_recursion


def ullman_v2(used_cols, current_row, G, P, M, M0, result=0, no_recursion=0):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.dot(M, G).T)):
            return result + 1, no_recursion
        else:
            return result, no_recursion
    for idx, el in enumerate(used_cols):
        if used_cols[idx] == 0 and M0[current_row][idx] == 1:
            M[current_row][idx] = 1
            for i in range(len(M[0])):
                if i != idx:
                    M[current_row][i] = 0
            used_cols[idx] = 1
            result, no_recursion = ullman_v2(used_cols, current_row + 1, G, P, M, M0, result, no_recursion + 1)
            used_cols[idx] = 0
    return result, no_recursion


def ullman_v3(used_cols, current_row, G, P, M, M0, result=0, no_recursion=0):
    if current_row == len(M):
        if np.array_equal(P, np.dot(M, np.dot(M, G).T)):
            return result + 1, no_recursion
        else:
            return result, no_recursion
    M_copy = copy(M)
    if current_row == M.shape[0] - 1:
        prune(G, P, M_copy)
    if current_row >= 1:
        for row in M_copy[:current_row]:
            if row.sum() == 0:
                return result, no_recursion
    for idx, el in enumerate(used_cols):
        if used_cols[idx] == 0 and M0[current_row][idx] == 1:
            for i in range(len(M[0])):
                if i != idx:
                    M_copy[current_row][i] = 0
            M_copy[current_row][idx] = 1
            used_cols[idx] = 1
            result, no_recursion = ullman_v3(used_cols, current_row + 1, G, P, M_copy, M0, result, no_recursion + 1)
            used_cols[idx] = 0
    return result, no_recursion


def prune(G, P, M):
    change = 1
    while True:
        if change == 0:
            return
        change = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    P_neigh = [k for k in range(len(P[i])) if P[i][k] == 1]
                    G_neigh = [k for k in range(len(G[j])) if G[j][k] == 1]
                    res = False
                    for x in P_neigh:
                        for y in G_neigh:
                            if M[x][y] == 1:
                                res = True
                    if not res:
                        change = 1
                        M[i][j] = 0


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    matrix_G = MatrixGraph()
    for i in graph_G:
        matrix_G.insertVertex(i[0])
        matrix_G.insertVertex(i[1])
    for i in graph_G:
        matrix_G.insertEdge(i[0], i[1])
    numpy_graph_G = matrix_G.toNumpy()

    matrix_P = MatrixGraph()
    for i in graph_P:
        matrix_P.insertVertex(i[0])
        matrix_P.insertVertex(i[1])
    for i in graph_P:
        matrix_P.insertEdge(i[0], i[1])
    numpy_graph_P = matrix_P.toNumpy()

    M1 = np.zeros((len(graph_P), len(graph_G)))
    M2 = np.zeros((len(graph_P), len(graph_G)))
    used_cols = np.zeros(len(graph_G))
    print(ullman(used_cols, 0, numpy_graph_G, numpy_graph_P, M1))

    M0 = np.zeros((len(matrix_P.lst), len(matrix_G.lst)))
    for i in range(len(matrix_P.lst)):
        for j in range(len(matrix_G.lst)):
            if len(matrix_P.neighbours(i)) <= len(matrix_G.neighbours(j)):
                M0[i][j] = 1

    print(ullman_v2(used_cols, 0, numpy_graph_G, numpy_graph_P, M1, M0))
    print(ullman_v3(used_cols, 0, numpy_graph_G, numpy_graph_P, M2, M0))


if __name__ == "__main__":
    main()
