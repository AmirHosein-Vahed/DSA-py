from ..linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.add_last(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")

        self.ll.delete_first()

    def peek(self):
        return self.ll.first.value

    def is_empty(self):
        return self.ll.is_empty()

    def __str__(self):
        return str(self.ll.first)
