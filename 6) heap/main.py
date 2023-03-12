class Element:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):    # <
        if self.priority < other.priority:
            return True
        elif self.priority > other.priority:
            return False

    def __gt__(self, other):    # >
        if self.priority > other.priority:
            return True
        elif self.priority < other.priority:
            return False

    def __str__(self):
        return str(self.priority) + ' : ' + str(self.data)


class Queue:
    def __init__(self):
        self.tab = []
        self.size = len(self.tab)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def peek(self):
        return self.tab[0]

    def dequeue(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            start = self.tab.pop(0)
            self.size -= 1
            return start
        else:
            self.size -= 1
            start = self.tab[0]
            self.tab[0] = self.tab.pop(-1)
            act = 0
            while True:
                if self.right(act) is None:
                    if self.left(act) is None:
                        return start
                    else:
                        self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                        act = self.left(act)
                        if self.left(act) is None:
                            return start
                elif self.tab[self.left(act)] > self.tab[self.right(act)]:
                    self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                    act = self.left(act)
                    if self.left(act) is None:
                        return start
                elif self.tab[self.right(act)] > self.tab[self.left(act)]:
                    self.tab[act], self.tab[self.right(act)] = self.tab[self.right(act)], self.tab[act]
                    act = self.right(act)
                    if self.right(act) is None:
                        return start
                else:
                    return start

    def enqueue(self, value, data):
        if self.size == 0:
            self.tab.append(Element(value, data))
            self.size = 1
            return
        else:
            self.tab.append(Element(value, data))
            act = self.size
            self.size += 1
            parent = self.parent(act)
            while act > 0 and self.tab[self.parent(act)] < self.tab[act]:
                self.tab[act] = self.tab[parent]
                act = parent
                parent = self.parent(act)
            self.tab[act] = Element(value, data)

    def left(self, index):
        if 2*index + 1 < self.size:
            return 2*index + 1
        else:
            return None

    def right(self, index):
        if 2*index + 2 < self.size:
            return 2*index + 2
        else:
            return None

    def parent(self, index):
        if self.size > index > 0:
            return int((index - 1)/2)
        else:
            return None

    def print_tab(self):
        print('{', end=' ')
        if self.size == 0:
            print('}')
        else:
            for i in range(self.size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx is None:
            return
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


A = Queue()
lst = [4, 7, 6, 7, 5, 2, 2, 1]
string = 'ALGORYTM'
for i in range(len(lst)):
    A.enqueue(lst[i], string[i])
A.print_tree(0, 0)
A.print_tab()
print(A.dequeue())
print(A.peek())
A.print_tab()
while A.size > 0:
    print(A.dequeue())
A.print_tab()
