from AVLTree import AVLTree


# 10
#   20
#     30
# 
# avl_tree = AVLTree(10)
# avl_tree.insert(20)
# avl_tree.insert(30)
# 10 is right heavy
# ////////////////////////////////////////
#     30
#   20
# 10
# 
# avl_tree = AVLTree(30)
# avl_tree.insert(20)
# avl_tree.insert(10)
# 30 is left heavy
# ////////////////////////////////////////
#     30
#    20
# 10    30
#     25
# 
# avl_tree = AVLTree(30)
# avl_tree.insert(20)
# avl_tree.insert(10)
# avl_tree.insert(25)
# 30 is left heavy

#       40
#    20   50
#   10 30   60
avl_tree = AVLTree(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(60)
# avl_tree.insert(70)
print("hi")