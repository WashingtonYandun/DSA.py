from SinglyLinkedList.Node import Node


class SiglyLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        link = self.head
        while link != None:
            print(link.data)
            link = link.link
