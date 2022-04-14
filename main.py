from data_structures.DoublyLinkedList import DoublyLinkedList
from data_structures.SinglyLinkedList import SinglyLinkedList


ll = SinglyLinkedList()
dll = DoublyLinkedList()

for i in range(10, 21, 1):
    dll.push(i)

dll.show()
print()
dll.reverse_i()
dll.reverse_show(dll.head)
dll.reverse_r()
print()
dll.show()
