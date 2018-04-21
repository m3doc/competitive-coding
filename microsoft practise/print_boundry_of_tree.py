class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None





def printLeftBoundary(root):

    if root:
        if(root.left):
            print root.data
            printLeftBoundary(root.left)
        elif(root.right):
            print root.data
            printLeftBoundary(root.right)




def printRightBoundary(root):

    if root:
        if root.right:
            printRightBoundary(root.right)
            print root.data
        elif root.left:
            printRightBoundary(root.left)
            print root.data





def printLeaves(root):
    if root:
        printLeaves(root.left)
        if (root.right == None and root.left == None):
            print root.data
        printLeaves(root.right)

def printBoundary(root):
    if (root):
        printLeftBoundary(root)
        printLeaves(root)
        printRightBoundary(root)

if __name__=="__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    printBoundary(root)