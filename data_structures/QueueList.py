class QueueList:
    queue = None

    def __init__(self):
        self.queue = []

    def add(self, new_data):
        self.queue.push(new_data)
        pass

    def peek(self):
        return self.queue[0]

    def poll(self):
        self.queue.remove(0)
        pass

    def size(self):
        return len(self.queue)

    def show(self):
        print(self.queue)
        pass
