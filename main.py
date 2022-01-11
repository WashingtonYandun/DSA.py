from SinglyLinkedList.Node import Node
from SinglyLinkedList.SiglyLinkedList import SiglyLinkedList


if __name__ == '__main__':
    # declare the link list
    listA = SiglyLinkedList()

    # declare the head of the list
    listA.head = Node(0)

    # declare the elements of the list
    e1 = Node(1)
    e2 = Node(2)

    # make the list
    listA.insertAtHead(100)
    e1.link = e2

    listA.show()
