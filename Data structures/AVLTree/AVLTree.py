class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return "Value=" + self.value


class AVLTree:
    def __init__(self, value):
        self.root = AVLNode(value)

    def insert(self, value):
        self.root = self.__insert(self.root, value)
    
    def __insert(self, root, value):
        if root == None:
            return AVLNode(value)

        if root.value > value:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)

        self.set_height(root)

        return self.balance(root)

    def balance(self, root):
        if self.is_left_heavy(root):
            if self.balance_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
                # print(f"{root.left.value} left rotaion")
            return self.rotate_right(root)
            # print(f"{root.value} right rotation")

        elif self.is_right_heavy(root):
            if self.balance_factor(root.right) > 0:
                root.right = self.rotate_right(root.right)
                # print(f"{root.right.value} right rotaion")
            return self.rotate_left(root)
            # print(f"{root.value} left rotation")
        
        return root

    def rotate_right(self, node):
        #     30 node
        #   20
        # 10  25
        new_node = node.left
        #     30 node
        #   20 new_node
        # 10  25
        node.left = new_node.right
        #     30 node
        #   25
        #   20 new_node
        # 10  25
        new_node.right = node
        #    
        #   20 new_node
        # 10  30
        #    25
        self.set_height(node)
        self.set_height(new_node)
        return new_node

    def rotate_left(self, node):
        # 10 node
        #    20
        # 15    30
        new_node = node.right
        # 10 node
        #    20 new_node
        # 15    30
        node.right = new_node.left
        # 10 node
        #  15
        #    20 new_node
        # 15    30
        new_node.left = node
        # 
        #    20 new_node
        # 10    30
        #   15
        self.set_height(node)
        self.set_height(new_node)
        return new_node


    def set_height(self, node):
        node.height = max(
            self.height(node.left),
            self.height(node.right)) + 1

    def is_left_heavy(self, node):
        return self.balance_factor(node) > 1

    def is_right_heavy(self, node):
        return self.balance_factor(node) < -1

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)


    def height(self, node):
        if node == None:
            return -1
        return node.height









