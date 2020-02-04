#Body
"""
    Get Node data of the Nth Node from the end.
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the node data of the linked list in the below method.
    """

def GetNode(head, position):
    count = 0
    final = 0
    new = head
    while(head.next!=None):
        final+=1
        head = head.next
    
    count = final-position
    while(count!=0):
        count-=1
        new = new.next
    return new.data