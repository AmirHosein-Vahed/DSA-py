from ..LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.__ll = LinkedList()

    def push(self, item):
        self.__ll.add_last(item)

    def pop(self):
        top = self.__ll.last.value
        self.__ll.delete_last()
        return top

    def peek(self):
        return self.__ll.last.value

    def is_empty(self):
        return self.__ll.is_empty()

    def __str__(self):
        return str(self.__ll.first)