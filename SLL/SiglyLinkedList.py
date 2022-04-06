from SLL.Node import Node


class SiglyLinkedList:
    head = None

    def __init__(self):
        self.head = None

    def insert_at(self, data, nth):
        pass

    def insert_at_Head(self, newData):
        self.head.link = Node(newData)

    def insert_at_end(self, newData):
        pass

    def delete_at(self, nth):
        pass

    def delete_at_end(self):
        pass

    def reverse(self):
        pass

    def reverse_r(self):
        pass

    def show(self):
        link = self.head
        while link != None:
            print(link.data)
            link = link.link

    def reverse_show(self):
        pass

    def len(self):
        currentNode = self.head
        l = 0
        while currentNode != None:
            l += 1
            currentNode = currentNode.link
        return l
