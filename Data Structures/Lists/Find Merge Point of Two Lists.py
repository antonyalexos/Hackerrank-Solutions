"""
    Find the node at which both lists merge and return the data of that node.
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    
    """

def FindMergeNode(headA, headB):
    initial = headB
    while(headA!=None):
        headA = headA.next
        headB = initial
        while(headB!=None):
            headB = headB.next
            if(headA == headB):
                return headA.data
        initial = initial.next











