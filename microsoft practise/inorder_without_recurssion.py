class Node:
    def __init__(self, value = 0):
        self.value = value
        self.right = None
        self.parent = None
        self.left = None





def inorder_traverse(root):
    S = []
    current = root
    while 1:
        while current != None:
            S.append(current)
            current = current.left

        if current == None and len(S) > 0:
            popped_node = S.pop()
            print popped_node.value,
            current = popped_node.right
        else:
            break







if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.parent = root

    root.right = Node(3)
    root.right.parent = root

    root.left.left = Node(4)
    root.left.left.parent = root.left

    root.left.right = Node(5)
    root.left.right.parent = root.left

    root.right.left = Node(6)
    root.right.left.parent = root.right

    root.right.right = Node(7)
    root.right.right.parent = root.right

    inorder_traverse(root)