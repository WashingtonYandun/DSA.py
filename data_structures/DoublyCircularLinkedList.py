class Dcll:
    data = None
    next = None
    prev = None
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    head = None

    def __init__(self, data):
        self.head = Dcll(data)