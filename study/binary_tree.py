from random import choice


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value:
            if value < self.value:
                if not self.left:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if not self.right:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


passed = [i for i in range(-10, 11)]
passed.remove(1)
tree = Node(1)
for _ in range(20):
    i = choice(passed)
    passed.remove(i)
    tree.insert(i)


def pre_order(root):
    if root:
        pre_order(root.left)
        print(root.value)
        pre_order(root.right)


pre_order(tree)