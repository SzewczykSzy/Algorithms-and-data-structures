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


class SelectionMethod:
    def __init__(self):
        self.tab = []
        self.size = len(self.tab)

    def insert(self, priority, data=None):
        self.tab.append(Element(priority, data))
        self.size += 1

    def swap_method(self):
        for i in range(self.size - 1):
            m = self.tab[i]
            for j in range(i, self.size):
                if self.tab[j] < m:
                    m = self.tab[j]
            index = 0
            for idx, el in enumerate(self.tab):
                if el is m:
                    index = idx
            self.tab[i], self.tab[index] = self.tab[index], self.tab[i]

    def shift_method(self):
        for i in range(self.size):
            m = self.tab[i]
            for j in range(i, self.size):
                if self.tab[j] > m:
                    m = self.tab[j]
            index = 0
            for idx, el in enumerate(self.tab):
                if el is m:
                    index = idx
            self.tab.insert(0, self.tab.pop(index))

    def print_tab(self):
        print('{', end=' ')
        if self.size == 0:
            print('}')
        else:
            for i in range(self.size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
            print('}')

    def test(self, lst, string, boool=False):
        t_start = time.perf_counter()
        for i in range(len(lst)):
            if isinstance(lst[i], tuple):
                self.insert(lst[i][0], lst[i][1])
            elif isinstance(lst[i], (int, float)):
                self.insert(lst[i])
        if string == "shift":
            self.shift_method()
        elif string == "swap":
            self.swap_method()
        if boool:
            self.print_tab()
        t_stop = time.perf_counter()
        print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
        print(" ")


def main():
    lst_1 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    B = SelectionMethod()
    A = SelectionMethod()
    print("swap: ")
    B.test(lst_1, "swap", True)
    print("shift: ")
    A.test(lst_1, "shift", True)

    lst_2 = []
    for x in range(0, 10000):
        lst_2.append(random.randint(0, 1000))
    C = SelectionMethod()
    D = SelectionMethod()
    print("swap: ")
    C.test(lst_2, "swap")
    print("shift: ")
    D.test(lst_2, "shift")
    print("Czas obliczeń dla sortowania kopcowego wynosi ok: 0.5")

if __name__ == "__main__":
    main()
