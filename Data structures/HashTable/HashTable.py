class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str("{"+str(self.key)+":"+str(self.value)+"} / " + str(self.next))


class HashTable:
    def __init__(self):
        self.first = None
        self.last = None


    def add(self, key, value):
        if self.is_empty():
            self.first = self.last = KeyValuePair(key, value)
            return

        current = self.first
        while(current != None):
            if current.key == key:
                current.value = value
                return

            current = current.next
        
        self.last.next = KeyValuePair(key, value)
        self.last = self.last.next

    
    def delete(self, key):
        if self.is_empty():
            raise Exception("empty")
        
        if self.first == self.last:
            if self.first.key == key:
                self.first = self.last = None
            return
        
        prev = self.first
        curr = self.first.next
        nex = self.first.next.next

        if prev.key == key:
            prev.next = None
            self.first = curr
            return

        while(curr != None):
            if curr.key == key:
                if self.last == curr:
                    self.last = prev

                curr.next = None
                prev.next = nex
            
            prev = curr
            curr = nex
            if nex != None:
                nex = nex.next

    
    def get_value(self, key):
        current = self.first
        while(current != None):
            if current.key == key:
                return current.value
            current = current.next
            
        return -1

    def is_empty(self):
        if self.first == self.last == None:
            return True
        return False

