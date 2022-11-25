from Tree import BSTree, Node

#        7
#    4       9
#  1  6    8  10
tree = BSTree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)

tree.print_nodes_at_distance(1)

#        7
#    4       9
#  1  6    8  10
#   2
# tree2 = BSTree()
# tree2.insert(7)
# tree2.insert(4)
# tree2.insert(9)
# tree2.insert(1)
# tree2.insert(6)
# tree2.insert(8)
# tree2.insert(10)
# tree2.insert(2)

# tree3 = BSTree()
# tree3.insert(10)
# tree3.root.left_child = Node(9)
# tree3.root.right_child = Node(12)
# print(tree3.is_BST())

# print(tree.equals(tree2))

# print(tree.height())
# print(tree.min())

# print(tree.find(8))

# tree.dfs_pre_order()
# tree.dfs_in_order()
# tree.dfs_post_order()

# print(tree.find(12))
# print(tree.root.value)
# print(tree.root.right_child.value)
# print(tree.root.left_child.value)

