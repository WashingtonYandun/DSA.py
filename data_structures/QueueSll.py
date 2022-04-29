from data_structures.SinglyLinkedList import SinglyLinkedList


class QueueSll:
    queue = None

    def __init__(self):
        self.queue = SinglyLinkedList()
        pass

    def add(self, new_data):
        self.queue.push(new_data)
        pass

    def peek(self):
        return self.queue.head.data

    def poll(self):
        self.queue.delete_end()
        pass

    def size(self):
        return self.queue.len()
