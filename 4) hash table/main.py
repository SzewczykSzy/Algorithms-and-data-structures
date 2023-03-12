import numbers


class KeyVal:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash_fun(self, par):
        if isinstance(par, (str, numbers.Number)):
            str_par = str(par)
            summ = 0
            for i in str_par:
                summ += ord(i)
            return summ % self.size
        else:
            return None

    def colision_method(self, key, i):
        return (self.hash_fun(key) + self.c1*i + self.c2*(i**2)) % self.size

    def search(self, key):
        for el in self.tab:
            if el:
                if key == el.key:
                    return el.value
        return None

    def insert(self, key, value):
        if self.tab[self.hash_fun(key)]:
            if self.tab[self.hash_fun(key)].key == key:
                self.tab[self.hash_fun(key)] = KeyVal(key, value)
                return
            else:
                for i in range(self.size):
                    if self.tab[self.colision_method(key, i)] is None:
                        self.tab[self.colision_method(key, i)] = KeyVal(key, value)
                        return
                print("Brak miejsca")
        else:
            self.tab[self.hash_fun(key)] = KeyVal(key, value)
        return

    def remove(self, key):
        if self.tab[self.hash_fun(key)]:
            self.tab[self.hash_fun(key)] = None
        else:
            print("Brak danej o podanym kluczu")

    def __str__(self):
        print('[', end='')
        for i in range(self.size):
            if self.tab[i]:
                print("{0}:{1}, ".format(self.tab[i].key, self.tab[i].value), end='')
            else:
                print("{0},".format(self.tab[i]), end=" ")
        print("]", end='')
        return ''


def first_test(c1, c2):
    A = HashTable(13, c1=c1, c2=c2)
    A.insert(1, 'A')
    A.insert(2, 'B')
    A.insert(3, 'C')
    A.insert(4, 'D')
    A.insert(5, 'E')
    A.insert(8, 'F')
    A.insert(9, 'G')
    A.insert(10, 'H')
    A.insert(11, 'I')
    A.insert(12, 'J')
    A.insert(13, 'K')
    A.insert(14, 'L')
    A.insert(15, 'M')
    A.insert(18, 'N')
    A.insert(31, 'O')
    print(A)
    print(A.search(5))
    print(A.search(14))
    A.insert(5, 'Z')
    print(A.search(5))
    A.remove(5)
    print(A)
    print(A.search(31))
    A.insert('test', 'W')
    print(A)


def second_test(c1, c2):
    A = HashTable(13, c1=c1, c2=c2)
    A.insert(13, 'A')
    A.insert(26, 'B')
    A.insert(39, 'C')
    A.insert(52, 'D')
    A.insert(65, 'E')
    A.insert(78, 'F')
    A.insert(91, 'G')
    A.insert(104, 'H')
    A.insert(117, 'I')
    A.insert(130, 'J')
    A.insert(143, 'K')
    A.insert(156, 'L')
    A.insert(169, 'M')
    A.insert(182, 'N')
    A.insert(195, 'O')
    print(A)


first_test(1, 0)
print('')
second_test(1, 0)
print('')
second_test(0, 1)
print('')
first_test(0, 1)
