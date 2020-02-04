"""
    Insert Node at a specific position in a linked list
    head input could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the head of the linked list in the below method.
    """
counter = 0
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if(position == 0):
        return Node(data,head)
    
    top = head
    prev = Node()
    new_node = Node(data,None)
    count = 0
    while top:
        count += 1
        prev = top
        top = top.next
        
        if count == position :
            prev.next = new_node
            new_node.next = top
            return head

"""def InsertNth(head, data, position)
    if position == 0:
        return Node(data, head)

    prevNode = head
    for _ in range(position-1):
        prevNode = prevNode.next
    prevNode.next = Node(data, prevNode.next)
    return head
"""




