"""
    Reverse a linked list
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the head of the linked list in the below method.
    """

def Reverse(head):
    prev = None
    while head:
        prev = Node(head.data, prev)
        head = head.next
    return prev