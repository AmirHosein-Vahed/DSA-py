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

    def is_empty(self) -> bool:
        return self.first == None

    def add_first(self, value) -> None:
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

    def add_last(self, value) -> None:
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def delete_first(self) -> None:
        node = self.first
        self.first = self.first.next
        node.next = None

    def delete_last(self) -> None:
        current = self.first
        while(True):
            if current.next == self.last:
                current.next = None
                self.last = current
                return

            current = current.next
            

    def contains(self, value) -> bool:
        current = self.first
        while(True):
            if current.value == value:
                return True
            
            if current.next == None:
                return False
            
            current = current.next
            

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
