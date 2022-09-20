from Queue import Queue

q = Queue()
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)

print(q.peek())
q.dequeue()
print(q.peek())
q.dequeue()
print(q.peek())

print(q)