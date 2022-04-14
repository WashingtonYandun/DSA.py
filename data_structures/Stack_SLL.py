from data_structures.SinglyLinkedList import SinglyLinkedList


class Stack_SLL:
    stk = None

    def __init__(self):
        self.stk = SinglyLinkedList()
        pass

    def push(self, data):
        self.stk.insert_at(data, self.size())
        return

    def do_pop(self):
        self.stk.delete_end()
        return

    def peek(self):
        return self.stk.peek()

    def size(self):
        return self.stk.lenght()

    def empty(self):
        if self.stk.lenght() == 0:
            return True
        if self.stk == None:
            return False
        return False

    def show(self):
        self.stk.show()
        return

    def search(self, data):
        for i in range(0, self.size(), 1):
            if self.stk[i] == data:
                return i
        return -1
