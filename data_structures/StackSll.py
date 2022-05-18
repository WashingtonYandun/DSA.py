from data_structures.SinglyLinkedList import SinglyLinkedList


class StackSll:
    stk = None

    def __init__(self, data):
        self.stk = SinglyLinkedList(data)
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
        return self.stk.length()

    def empty(self):
        if self.stk.length() == 0:
            return True
        if self.stk is None:
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
