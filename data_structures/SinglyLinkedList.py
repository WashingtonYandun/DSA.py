class SLL_Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    head = None

    def __init__(self, head=None):
        self.head = None

    def lenght(self):
        if self.head is None:
            print("Just the head")
            return 1
        aux = self.head
        l = 0
        while aux is not None:
            l += 1
            aux = aux.next
        return l

    def push(self, newData):
        new_node = SLL_Node(newData)
        if self.head is None:
            self.head = new_node
            return
        aux = self.head
        while aux.next is not None:
            aux = aux.next
        aux.next = new_node
        pass

    def change_head(self, new_data):
        temp = self.head
        new_node = SLL_Node(new_data)
        new_node.next = temp.next
        del self.head
        self.head = new_node
        pass

    def insert_at(self, new_data, nth):
        if nth > self.lenght() or nth < 0:
            print("Invalid Position")
            return

        aux = self.head
        new_node = SLL_Node(new_data)

        if nth == 0:
            new_node.next = aux
            self.head = new_node
            return
        for i in range(0, nth - 1, 1):
            aux = aux.next
        new_node.next = aux.next
        aux.next = new_node
        pass

    def delete_end(self):
        aux = self.head
        while aux.next.next is not None:
            aux = aux.next
        temp = aux.next.data
        del aux.next
        aux.next = None
        return temp

    def delete_at(self, nth):
        aux = self.head
        if nth > self.lenght() or nth < 0:
            print("Invalid Position")
            return
        if nth == 0:
            del self.head
            aux.next = self.head
            return
        if nth == self.lenght():
            self.delete_end()
            return
        for i in range(0, nth - 1, 1):
            aux = aux.next
        temp = aux.next
        del aux.next
        aux.next = temp.next
        pass

    def peek(self):
        aux = self.head
        while aux.next is not None:
            aux = aux.next
        return aux.data

    def reverse_i(self):
        current = self.head
        prev = None
        while current is not None:
            prox = current.next
            current.next = prev
            prev = current
            current = prox
        self.head = prev
        pass

    def reverse_r(self, current):
        # TODO: solve recursive reverse method
        if current.next is None:
            self.head = current
            return
        return self.reverse_r(current.next)

    def reverse_show(self, aux):
        if aux.next != None:
            print(aux.data)
            self.reverse_print(aux.next)
        return

    def show(self):
        if self.head is None:
            print("Head is None, no more elements")
            return

        aux = self.head

        while aux is not None:
            print(aux.data)
            aux = aux.next
        pass
