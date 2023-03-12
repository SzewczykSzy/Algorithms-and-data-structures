class RootNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BstTree:
    def __init__(self):
        self.head = None
        self.heigh = 0

    def search(self, key, node):
        if node is None:
            return "drzewo jest puste"
        else:
            if key < node.key:
                return self.search(key, node.left)
            elif key > node.key:
                return self.search(key, node.right)
            elif key == node.key:
                return node.value

    def insert(self, key, value, node):
        if self.head is None:
            self.head = RootNode(key, value)
            return
        else:
            if node is None:
                return RootNode(key, value)
            if key < node.key:
                node.left = self.insert(key, value, node.left)
                return node
            elif key > node.key:
                node.right = self.insert(key, value, node.right)
                return node
            elif key == node.key:
                node.value = value
                return node

    def delete(self, key, node):
        if self.head is None:
            return print("drzewo jest puste")
        else:
            if key < node.key:
                node.left = self.delete(key, node.left)
                return node
            elif key > node.key:
                node.right = self.delete(key, node.right)
                return node
            elif key == node.key:
                if all([node.left, node.right]) is None:
                    node = None
                    return node
                elif node.right is None and node.left:
                    node.key = node.left.key
                    node.value = node.left.value
                    node.left = node.left.left
                    node.right = None
                    return node
                elif node.left is None and node.right:
                    node.key = node.right.key
                    node.value = node.right.value
                    node.left = None
                    node.right = node.right.right
                    return node
                elif node.left and node.right:
                    elem, prev = self.delete_nested(node.right)
                    if prev is None:
                        node.key = elem.key
                        node.value = elem.value
                        node.right = elem.right
                    else:
                        node.key = elem.key
                        node.value = elem.value
                        prev.left = elem.right
                    return node
            else:
                return print("brak danej o takim kluczu")

    def delete_nested(self, node, prev=None):
                if node.left is None:
                    return node, None
                elif node.left.left is None:
                    return node.left, node
                elif node.left is not None:
                    return self.delete_nested(node.left, node)

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self._print_tree(node.left, lvl + 5)

    def print_sorted(self):
        print("[", end="")
        self.print_sorted_nested(self.head)
        print("]")

    def print_sorted_nested(self, node):
        if node is not None:
            self.print_sorted_nested(node.left)
            print(" {0}:{1} ".format(node.key, node.value), end="")
            self.print_sorted_nested(node.right)

    def height(self):
        return self.height_nested(self.head)

    def height_nested(self, node, sum=-2):
        sum += 1
        if node is not None:
            self.height_nested(node.left, sum)
            self.height_nested(node.right, sum)
        if sum > self.heigh:
            self.heigh = sum
        sum -= 1
        return self.heigh

A = BstTree()
lista = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
for i in lista:
    A.insert(i, lista[i], A.head)
A.print_tree()
A.print_sorted()
print(A.search(24, A.head))
A.insert(20, 'AA', A.head)
A.insert(6, 'M', A.head)
A.delete(62, A.head)
A.insert(59, 'N', A.head)
A.insert(100, 'P', A.head)
A.delete(8, A.head)
A.delete(15, A.head)
A.insert(55, 'R', A.head)
A.delete(50, A.head)
A.delete(5, A.head)
A.delete(24, A.head)
print(A.height())
A.print_sorted()
A.print_tree()
