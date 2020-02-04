"""
    Node is defined as
    self.left (the left child of the node)
    self.right (the right child of the node)
    self.data (the value of the node)
    """
def preOrder(root):
    print(root.data),
    if(root.left!=None):
        preOrder(root.left)
    if(root.right!=None):
        preOrder(root.right)




