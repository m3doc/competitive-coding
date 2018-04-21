class Node:
    def __init__(self, data):
        self.value = data
        self.nextNode = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next_node(self):
        return self.nextNode

    def set_next_node(self, value):
        self.nextNode = value



class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size



