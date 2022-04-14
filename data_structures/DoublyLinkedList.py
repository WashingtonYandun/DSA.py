class DLL_Node:
    def __init__(self, data=0,  prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:

    head = None

    def __init__(self, head=None):
        self.head = head

    def lenght(self):
        aux = self.head
        l = 0
        while aux.next != None:
            l += 1
            aux = aux.next
        return l

    def push(self, newData):
        newNode = DLL_Node(newData)
        if self.head == None:
            self.head = newNode
            return

        aux = self.head

        while aux.next != None:
            aux = aux.next

        newNode.prev = aux.next
        aux.next = newNode
        newNode.next = None

    def change_head(self, newData):
        pass

    def insert_at(self, newData, nth):
        pass

    def delete_end(self):
        pass

    def delete_at(self, nth):
        pass

    def peek(self):
        aux = self.head
        while aux.next != None:
            aux = aux.next
        return aux.data

    def reverse_i(self):
        current = self.head
        prev = current.prev
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        pass

    def reverse_show(self, aux):
        if(aux.next != None):
            print(aux.data)
            self.reverse_show(aux.next)
        return

    def show(self):
        if self.head == None:
            print("Head is None, no more elements")
            return

        aux = self.head

        while aux != None:
            print(aux.data)
            aux = aux.next
