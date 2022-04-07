from data_structures.SinglyLinkedList import SinglyLinkedList


ll = SinglyLinkedList()

for i in range(0, 10, 1):
    ll.push(i)

ll.show()
print("")

ll.reverse_r(ll.head)
ll.show()
print()

print(ll.lenght())
