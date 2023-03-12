import random
import time


class Element:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):  # <
        if self.priority < other.priority:
            return True
        elif self.priority > other.priority:
            return False

    def __gt__(self, other):  # >
        if self.priority > other.priority:
            return True
        elif self.priority < other.priority:
            return False

    def __eq__(self, other):
        if self.priority == other.priority:
            return True
        else:
            return False

    def __str__(self):
        if self.data is None:
            return str(self.priority)
        else:
            return str(self.priority) + ':' + str(self.data)


class Queue:
    def __init__(self):
        self.tab = []
        self.size = len(self.tab)
        self.size_2 = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def peek(self):
        return self.tab[0]

    def dequeue_1(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            return None
        else:
            for act in range(self.parent(self.size - 1), -1, -1):
                while True:
                    if self.right(act) is None:
                        if self.left(act) is None:
                            break
                        else:
                            if self.tab[act] < self.tab[self.left(act)]:
                                self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                                break
                            else:
                                break
                    elif self.tab[act] < self.tab[self.right(act)] or self.tab[act] < self.tab[self.left(act)]:
                        if self.tab[self.left(act)] > self.tab[self.right(act)]:
                            self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                            act = self.left(act)
                            if self.left(act) is None:
                                break
                        elif self.tab[self.right(act)] > self.tab[self.left(act)]:
                            self.tab[act], self.tab[self.right(act)] = self.tab[self.right(act)], self.tab[act]
                            act = self.right(act)
                            if self.right(act) is None:
                                break
                        elif self.tab[self.right(act)] == self.tab[self.left(act)]:
                            self.tab[act], self.tab[self.right(act)] = self.tab[self.right(act)], self.tab[act]
                            act = self.right(act)
                            if self.right(act) is None:
                                break
                        else:
                            break
                    else:
                        break

    def dequeue_2(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            return None
        else:
            while True:
                self.size_2 -= 1
                if self.tab[0].priority >= self.tab[self.size_2].priority:
                    self.tab[0], self.tab[self.size_2] = self.tab[self.size_2], self.tab[0]
                act = 0
                while True:
                    if self.right(act) is None:
                        if self.left(act) is None:
                            break
                        else:
                            if self.tab[act] < self.tab[self.left(act)] and self.left(act) < self.size_2:
                                self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                                break
                            else:
                                break
                    elif self.tab[act] < self.tab[self.right(act)] or self.tab[act] < self.tab[self.left(act)]:
                        if self.tab[self.left(act)] > self.tab[self.right(act)]:
                            if self.left(act) < self.size_2:
                                self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                                act = self.left(act)
                                if self.left(act) is None:
                                    break
                            else:
                                break
                        elif self.tab[self.right(act)] > self.tab[self.left(act)]:
                            if self.right(act) < self.size_2:
                                self.tab[act], self.tab[self.right(act)] = self.tab[self.right(act)], self.tab[act]
                                act = self.right(act)
                                if self.right(act) is None:
                                    break
                            elif self.left(act) < self.size_2:
                                self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                                act = self.left(act)
                                if self.left(act) is None:
                                    break
                            else:
                                break
                        elif self.tab[self.right(act)] == self.tab[self.left(act)]:
                            if self.right(act) < self.size_2:
                                self.tab[act], self.tab[self.right(act)] = self.tab[self.right(act)], self.tab[act]
                                act = self.right(act)
                                if self.right(act) is None:
                                    break
                            elif self.left(act) < self.size_2:
                                self.tab[act], self.tab[self.left(act)] = self.tab[self.left(act)], self.tab[act]
                                act = self.right(act)
                                if self.right(act) is None:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if self.size_2 == 1:
                    break

    def enqueue(self, priority, data=None):
        self.tab.append(Element(priority, data))
        self.size += 1
        self.size_2 += 1

    def heapify(self, lst, boool):
        for i in range(len(lst)):
            if isinstance(lst[i], tuple):
                self.enqueue(lst[i][0], lst[i][1])
            elif isinstance(lst[i], (int, float)):
                self.enqueue(lst[i])
        if boool:
            self.print_tab()
            self.print_tree(0, 0)
        self.dequeue_1()
        self.dequeue_2()
        if boool:
            self.print_tab()

    def left(self, index):
        if 2 * index + 1 < self.size:
            return 2 * index + 1
        else:
            return None

    def right(self, index):
        if 2 * index + 2 < self.size:
            return 2 * index + 2
        else:
            return None

    def parent(self, index):
        if self.size > index > 0:
            return int((index - 1) / 2)
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


def main():
    lst_1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    t_start = time.perf_counter()
    print(lst_1)
    A = Queue()
    A.heapify(lst_1, True)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}\n".format(t_stop - t_start))

    lst_2 = []
    for x in range(0, 10000):
        lst_2.append(random.randint(0, 99))
    t_start = time.perf_counter()
    B = Queue()
    B.heapify(lst_2, False)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()