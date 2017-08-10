class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("apple")
q.enqueue("10")
q.enqueue("false")
# LOL, this is what happens if you print q itself.
print(q)
print(q.items)
print(q.size())
print(q.isEmpty())
q.dequeue()
q.dequeue()
print(q.size())

