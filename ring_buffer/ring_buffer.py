class RingBuffer:
    def __init__(self, capacity):
        self.value = 0
        self.capacity = capacity
        self.storage = [None for x in range(0, capacity)]

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.value = 0
            self.storage.append(item)
            self.storage[self.value] = item
        else:
            self.value = (self.value + 1) % self.capacity

    def get(self):
        return [x for x in self.storage ]

