class Node:
    def __init__(self, value):
        # left < node < right
        self.value = value
        self.right_child = None
        self.left_child = None
        #        7
        #    4       9
        #  1  6    8  10

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return 

        current = self.root
        while(True):
            if current.value == value:
                raise Exception("equal")

            elif value < current.value:
                if current.left_child == None:
                    current.left_child = Node(value)
                    return
                current = current.left_child

            else:
                if current.right_child == None:
                    current.right_child = Node(value)
                    return
                current = current.right_child


    def find(self, value) -> bool:
        current = self.root
        while(current != None):
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True
            
        return False

    
    def dfs_pre_order(self):
        self.__traverse_pre_order(self.root)

    def dfs_in_order(self):
        self.__traverse_in_order(self.root)

    def dfs_post_order(self):
        self.__traverse_post_order(self.root)


    def __traverse_pre_order(self, root):
        if root == None:
            return
        print(root.value)
        self.__traverse_pre_order(root.left_child)
        self.__traverse_pre_order(root.right_child)
 
 
    def __traverse_in_order(self, root):
        if root == None:
            return
        self.__traverse_pre_order(root.left_child)
        print(root.value)
        self.__traverse_pre_order(root.right_child)


    def __traverse_post_order(self, root):
        if root == None:
            return
        self.__traverse_pre_order(root.left_child)
        self.__traverse_pre_order(root.right_child)
        print(root.value)
            
        