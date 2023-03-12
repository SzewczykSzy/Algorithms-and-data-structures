class Queue:
    def __init__(self, size=5):
        self.size = size
        self.tab = [None for i in range(size)]
        self.read_index = self.record_index = 0

    def realloc(self):
        old_size = len(self.tab)
        self.record_index = self.size
        self.size *= 2
        return [self.tab[i] if i < old_size else None for i in range(self.size)]

    def is_empty(self):
        return self.read_index == self.record_index

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.read_index = (self.read_index + 1) % self.size
            return self.tab[self.read_index - 1]

    def enqueue(self, data):
        self.tab[self.record_index] = data
        self.record_index = (self.record_index + 1) % self.size
        if self.record_index == self.read_index:
            self.tab = self.realloc()
            temp_tab = self.tab[self.read_index:int(self.size/2)]
            for i in range(self.read_index, int(self.size/2)):
                self.tab[i] = None
                for j in range(0, len(temp_tab)):
                    self.tab[-j - 1] = temp_tab[-j - 1]
            index_change = [self.read_index, self.record_index]
            self.read_index = index_change[1] + index_change[0]
            self.record_index = index_change[0]

    def tab_to_str(self):
        if self.record_index == self.read_index:
            print("table: [ ]")
        else:
            print("table: [", end="")
            for i in range(self.size):
                print(self.tab[i], end=" ")
            print("]")

    def que_to_str(self):
        if self.record_index == self.read_index:
            print("queue: [ ]")
        elif self.record_index > self.read_index:
            print("queue: [", end="")
            for i in range(self.read_index, self.record_index):
                print(self.tab[i], end=" ")
            print("]")
        else:
            print("queue: [", end="")
            for i in range(self.read_index, self.size):
                print(self.tab[i], end=" ")
            for i in range(0, self.record_index):
                print(self.tab[i], end=" ")
            print("]")


def pri(que:Queue):
    que.tab_to_str()
    que.que_to_str()
    print("")


A = Queue()
pri(A)
for i in range(4):
    A.enqueue(i+1)
pri(A)
print("pierwsza wpisana: ", A.dequeue())
print("druga wpisana: ", A.peek())
print("")
pri(A)
for i in range(4, 8):
    A.enqueue(i+1)
pri(A)
for i in range(A.size - A.read_index + A.record_index):
    print(A.dequeue())
pri(A)
A.enqueue(99)
pri(A)
