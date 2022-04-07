class SLL_Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = None

    def lenght(self):
        if self.head == None:
            print("Just the head")
            return 1

        aux = self.head
        l = 0
        while aux != None:
            l += 1
            aux = aux.next

        return l

    def push(self, newData):
        newNode = SLL_Node(newData)
        if self.head == None:
            self.head = newNode
            return

        aux = self.head
        while aux.next != None:
            aux = aux.next

        aux.next = newNode

    '''
    def change_head(self, newData):
        temp = self.head
        newNode = SLL_Node(newData)
        newNode.next = temp.next

        del self.head

        self.head = newNode
        pass
    '''

    def insert_at(self, newData, nth):
        if nth > self.lenght() or nth < 0:
            print("Invalid Position")
            return

        aux = self.head
        newNode = SLL_Node(newData)

        if nth == 0:
            newNode.next = aux
            self.head = newNode
            return

        for i in range(0, nth - 1, 1):
            aux = aux.next

        newNode.next = aux.next
        aux.next = newNode

    def show(self):
        if self.head == None:
            print("Head is None, no more elements")
            return

        aux = self.head

        while aux != None:
            print(aux.data)
            aux = aux.next
