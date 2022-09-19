class Array:
    def __init__(self, size: int, value=None):
        self.array = [value]*size
        self.index = -1

    def __str__(self):
        return str(self.array)

    def append(self, item):
        if self.index == len(self.array)-1:
            new_array = [None]*(len(self.array)*2)
            for index, element in enumerate(self.array):
                new_array[index] = element
            self.index += 1
            new_array[self.index] = item
            self.array = new_array
        else:
            self.index += 1
            self.array[self.index] = item

    def remove_at(self, index: int):
        if index > len(self.array)-1:
            raise Exception("index out of range")

        for ind in range(index, len(self.array)-1):
            self.array[ind] = self.array[ind+1]
        self.array[-1] = None