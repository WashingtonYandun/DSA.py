class DllNode:
    def __init__(self, data=0, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    head = None

    def __init__(self, head=None):
        self.head = head

    def length(self):
        aux = self.head
        l = 0
        while aux.next is not None:
            l += 1
            aux = aux.next
        return l

    def push(self, new_data):
        prev = None
        new_node = DllNode(new_data)
        if self.head is None:
            self.head = new_node
            return

        aux = self.head

        while aux.next is not None:
            aux.prev = prev
            prev = aux
            aux = aux.next

        aux.prev = prev
        new_node.prev = aux
        aux.next = new_node
        new_node.next = None
        pass

    def change_head(self, new_data):
        pass

    def insert_at(self, new_data, nth):
        new_node = DllNode(new_data)
        aux = self.head

        if nth >= self.length() or nth < 0:
            print("Invalid Position")
            return

        if nth == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return

        if nth == self.length() - 1:
            self.push(new_data)
            return

        for i in range(0, nth - 1, 1):
            aux = aux.next

        aux.next.prev = new_node
        new_node.next = aux.next
        aux.next = new_node
        new_node.prev = aux
        pass

    def delete_end(self):
        pass

    def delete_at(self, nth):
        pass

    def peek(self):
        aux = self.head
        while aux.next is not None:
            aux = aux.next
        return aux.data

    def reverse_i(self):
        current = self.head
        prev = current.prev
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        pass

    def reverse_show(self, aux):
        if aux.next is not None:
            print(aux.data)
            self.reverse_show(aux.next)
        return

    def show(self):
        if self.head is None:
            print("Head is None, no more elements")
            return

        aux = self.head

        while aux is not None:
            print(aux.data)
            aux = aux.next
