class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) < self.storage:
            self.storage.append(item)
            self.size += 1
        else:
            self.storage[self.size] = item
            self.size = ((self.size + 1) % self.capacity)

    def get(self):
        storage = []
        for x in self.storage:
            if x is not None:
                storage.append(x)
        return storage
