from Tree import BSTree

tree = BSTree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)

# print(tree.find(8))

# tree.dfs_pre_order()
# tree.dfs_in_order()
tree.dfs_post_order()

# print(tree.find(12))
# print(tree.root.value)
# print(tree.root.right_child.value)
# print(tree.root.left_child.value)

