#Validate if a binary tree is a binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def isBST(self):
        arr = self.inorderTraversal(self.root) 
        for i in range(len(arr)-1):
            return arr[i] < arr[i+1]
            
    def inorderTraversal(self,root):
        arr = []
        if root:
            arr = self.inorderTraversal(root.left)
            arr.append(root.value)
            arr = arr + self.inorderTraversal(root.right)
        return arr
        
        
 #      30
#     /  \
#   20   50
#  / \   / \
# 15 25 45 80

tree = BinaryTree(30)
tree.root.left = Node(20)
tree.root.right = Node(50)
tree.root.left.left = Node(15)
tree.root.left.right = Node(25)
tree.root.right.right = Node(80)
tree.root.right.left = Node(45)
tree.isBST()


#      10
#     /  \
#   45   20
#  / \   / \
# 50 60 15 5

tree = BinaryTree(10)
tree.root.left = Node(45)
tree.root.right = Node(20)
tree.root.left.left = Node(50)
tree.root.left.right = Node(60)
tree.root.right.right = Node(15)
tree.root.right.left = Node(5)
tree.print_inorder()
tree.isBST()
