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


# Uncomment below if you want to test

# q = Queue()
# q.enqueue("apple")
# q.enqueue("10")
# q.enqueue("false")
# # LOL, this is what happens if you print q itself.
# print(q)
# print(q.items)
# print(q.size())
# print(q.isEmpty())
# q.dequeue()
# q.dequeue()
# print(q.size())


# print("HOTPOTATO TIME!")

# # implementation of hotpotatoes
# def hotPotato(namelist, num):
#     # we make a queue
#     nq = Queue()
#     # going through the list and adding into the queue
#     for name in namelist:
#         nq.enqueue(name)
#     print("Starting list: " + str(nq.items))
#     # while we still have things in the queue
#     while nq.size() > 1:
#         # goes through the loop based on num
#         for i in range(num):
#             # pops and add back into the queue
#             nq.enqueue(nq.dequeue())
#             # print(nq.items)
#         # after we exit the loop, we pop out the next one which is the laast
#         print(nq.items)
#         nq.dequeue()
#     # and we then pop out the last survivor and return the winner
#     return nq.dequeue()

# print(hotPotato(["Sue", "Justin", "Fina", "Guido", "Gadwin"], 4))