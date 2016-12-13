class Node:
    def __init__(self,value):
        self.value = value
class linkedList:
    def __init__(self,node):
        self.head = node
        self.current = node
        self.next = None
    def insert(self,node2):
        self.current.next = node2
        self.current = node2
        self.current.next =None




currentNode = Node(1)
ll = linkedList(currentNode)
for i in xrange(2,5):
    nextNode = Node(i)
    ll.insert(nextNode)
node = ll.head
# print node.value
# print node.next
while node.next!=None:
    print node.value
    node = node.next








