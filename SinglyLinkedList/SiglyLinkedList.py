from SinglyLinkedList.Node import Node


class SiglyLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        link = self.head
        while link != None:
            print(link.data)
            link = link.link

    def insertAtHead(self, newData):
        self.head.link = Node(newData)
