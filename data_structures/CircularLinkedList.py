class CllNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    head = None

    def __init__(self, data=None):
        self.head = CllNode(data)
        self.head = None


    def length(self):
        if self.head is None:
            return 0


    def push(self, new_data):
        pass

    def change_head(self, new_data):
        pass

    def insert_at(self, new_data, nth):
        pass

    def delete_end(self):
        pass

    def delete_at(self, nth):
        pass

    def peek(self):
        pass

    def reverse_i(self):
        pass

    def reverse_r(self, current):
        pass

    '''
    def reverse_show(self, aux):
        pass
    '''

    def show(self):
        pass