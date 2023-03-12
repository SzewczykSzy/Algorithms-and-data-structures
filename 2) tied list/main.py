from copy import deepcopy

class ElementOfList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, added):
        new_elem = self.head
        self.head = ElementOfList(added, new_elem)

    def remove(self):
        if self.head is not None:
            head_val = self.head
            self.head = self.head.next
            head_val = None
        else:
            pass

    def is_empty(self):
        return print(self.head is None)

    def length(self):
        node = self.head
        sum = 0
        while node is not None:
            sum += 1
            node = node.next
        return sum

    def get(self):
        return self.head.data

    def to_str(self):
        node = self.head
        print("[", end="")
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print("]")

    def remove_end(self):
        node = self.head
        if self.length() == 1:
            head_val = self.head
            self.head = self.head.next
            head_val = None
        elif node is not None:
            while True:
                if node.next.next is None:
                    node.next = None
                    return
                node = node.next
        else:
            print("Lista jest pusta")

    def add_to_end(self, item):
        node = self.head
        if node is not None:
            node = self.head
            while True:
                if node.next is None:
                    node.next = ElementOfList(item)
                    return
                node = node.next
        else:
            self.head = ElementOfList(item)

    def take(self, n):
        new_list = LinkedList()
        node = self.head
        for i in range(n):
            new_list.add_to_end(node.data)
            if node.next is None:
                break
            node = node.next
        return new_list

    def drop(self, n):
        new_list = deepcopy(self)
        for i in range(n):
            new_list.remove()
        return new_list


Lista = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364), ('PW', 'Warszawa', 1915), ('UW', 'Warszawa', 1915), ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]

A = LinkedList()
A.add(('PW', 'Warszawa', 1915))
A.to_str()
A.add(('UJ', 'Kraków', 1364))
A.add(('KPU', 'Krosno', 1999))
A.to_str()
A.remove()
A.add(('AGH', 'Kraków', 1919))
A.add_to_end(('UW', 'Warszawa', 1915))
A.add_to_end(('UP', 'Poznań', 1919))
A.add_to_end(('PG', 'Gdańsk', 1945))
A.add_to_end(('UR', 'Rzeszów', '2001'))
A.to_str()
A.remove_end()
A.to_str()
print("Pierwszy element: ", A.get())
B = A.drop(8)
B.to_str()
print("Długośc: ", A.length())
C = A.take(2)
C.to_str()
A.destroy()
A.is_empty()

