class Stack_List:
    stk = None

    def __init__(self):
        self.stk = []

    def push(self, data):
        self.stk.append(data)

    def do_pop(self):
        self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def size(self):
        return len(self.stk)

    def empty(self):
        if self.stk == []:
            return True
        return False

    def search(self, data):
        for i in range(0, self.size(), 1):
            if self.stk[i] == data:
                return i
        return -1

    def show(self):
        for i in range(0, self.stk.size(), 1):
            print(self.stk[i])
        return
