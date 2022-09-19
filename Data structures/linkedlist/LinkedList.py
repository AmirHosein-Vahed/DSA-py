import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str("value:" + str(self.value) + " / next:" + str(self.next))


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.first == None

    def add_first(self, value) -> None:
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

        self.__size += 1

    def add_last(self, value) -> None:
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        
        self.__size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("linkedlist is empty")

        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.next
            self.first.next = None
            self.first = second

        self.__size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("linkedlist is empty")

        if self.first == self.last:
            self.first = self.last = None
        else:
            current = self.first
            while(True):
                if current.next == self.last:
                    current.next = None
                    self.last = current
                    break

                current = current.next
        
        self.__size -= 1

    def contains(self, value) -> bool:
        return self.index_of(value) != -1
            
    def index_of(self, value):
        current = self.first
        index = 0
        while(True):
            if current.value == value:
                return index

            if current.next == None:
                return -1

            current = current.next
            index += 1

    def size(self):
        return self.__size

    def to_array(self):
        if self.is_empty():
            return []

        arr = []
        current = self.first
        while(True):
            arr.append(current.value)

            if current.next == None:
                return arr

            current = current.next

    def reverse(self):
        if self.is_empty():
            return
        if self.first == self.last:
            return

        prev = self.first
        curr = self.first.next
        nex  = self.first.next.next
    
        while(True):
            if curr == None:
                self.last = self.first
                self.last.next = None
                self.first = prev
                return

            curr.next = prev

            prev = curr
            curr = nex
            if nex != None:
                nex  = nex.next

    def kth_from_end(self, k: int):
        if self.is_empty():
            raise Exception("linkedlist is empty")
            
        if k > self.__size:
            raise Exception("index out of range")

        a = self.first
        b = self.first
        for i in range(k-1):
            b = b.next
        
        while(True):
            if b == self.last:
                return a.value
            
            a = a.next
            b = b.next
