import polska


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


class ListGraph:
    def __init__(self):
        self.lst = []
        self.dict_graph = {}
        self.dictionary = {}

    def insertVertex(self, vertex):
        vertex = Node(vertex)
        if vertex.key in self.lst:
            pass
        else:
            self.lst.append(vertex.key)
            self.dictionary[vertex.key] = len(self.lst) - 1
            self.dict_graph[vertex.key] = []

    def insertEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1.key in self.lst and vertex2.key in self.lst:
            if vertex1.key not in self.dict_graph[vertex2.key] and vertex2.key not in self.dict_graph[vertex1.key]:
                self.dict_graph[vertex1.key].append(vertex2.key)
                self.dict_graph[vertex2.key].append(vertex1.key)
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
            temp_lst = self.dict_graph[vertex.key]
            del self.dict_graph[vertex.key]
            for key in self.dict_graph.keys():
                if key in temp_lst:
                    self.dict_graph[key].remove(vertex.key)
        else:
            pass

    def deleteEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        if vertex1.key in self.lst and vertex2.key in self.lst:
            if vertex1.key in self.dict_graph[vertex2.key] and vertex2.key in self.dict_graph[vertex1.key]:
                self.dict_graph[vertex1.key].remove(vertex2.key)
                self.dict_graph[vertex2.key].remove(vertex1.key)

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

    def order(self):
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


def test(graph):
    for i in polska.polska:
        graph.insertVertex(i[2])
    for i in polska.graf:
        graph.insertEdge(i[0], i[1])
    print(graph.dict_graph)
    graph.deleteVertex('K')
    graph.deleteEdge("W", 'E')
    polska.draw_map(graph.edges())


def main():
    graph_1 = MatrixGraph()
    graph_2 = ListGraph()

    # test(graph_1)
    test(graph_2)


if __name__ == "__main__":
    main()
