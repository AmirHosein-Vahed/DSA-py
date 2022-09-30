class Node:
    def __init__(self, value):
        # left < node < right
        self.value = value
        self.right_child = None
        self.left_child = None


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

    def print_nodes_at_distance(self, distance):
        return self.__print_nodes_at_distance(distance, self.root)

    def __print_nodes_at_distance(self, distance, root):
        if root == None:
            return
            
        if distance == 0:
            print(root.value)
            return
        
        self.__print_nodes_at_distance(distance-1, root.left_child)
        self.__print_nodes_at_distance(distance-1, root.right_child)




    def is_BST(self):
        return self.__validate(self.root, float('-inf'), float('+inf'))

    def __validate(self, root, minimum, maximum):
        if root == None:
            return True
        
        if not (minimum < root.value < maximum):
            return False
        
        return self.__validate(root.left_child, minimum, root.value) and\
               self.__validate(root.right_child, root.value, maximum)

    
    def equals(self, tree):
        return self.__equals(self.root, tree.root)

    def __equals(self, root1, root2):
        if root1 == root2 == None:
            return True
        
        if root1 != None and root2 != None:
            return root1.value == root2.value and \
                self.__equals(root1.left_child, root2.left_child) and \
                self.__equals(root1.right_child, root2.right_child)
        
        return False

    
    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root == None:
            return -1
        # if root.left_child == root.right_child == None:
        #     return 0
        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))


    def min(self):
        # for BST:
        # current = self.root
        # last    = current
        # while(current != None):
        #     last = current
        #     current = current.left_child
        # return last.value

        return self.__min(self.root)

    def __min(self, root):
        if root.left_child == root.right_child == None:
            return root.value
        
        elif root.left_child == None:
            right = self.__min(root.right_child)
            return min(right, root.value)

        elif root.right_child == None:
            left  = self.__min(root.left_child)
            return min(left, root.value)

        else:
            left  = self.__min(root.left_child)
            right = self.__min(root.right_child)
            return min(left, right, root.value)

    
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
            
        