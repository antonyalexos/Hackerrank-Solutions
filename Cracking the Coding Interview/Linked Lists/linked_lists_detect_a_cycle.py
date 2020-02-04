"""
    Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
    
    A Node is defined as:
    
    class Node(object):
    def __init__(self, data = None, next_node = None):
    self.data = data
    self.next = next_node
    """


def has_cycle(head):
    pass
    if(head==None):
        return 0
    array = []
    while(head.next != None):
        if(head in array):
            return 1
        else:
            array.append(head)
        head = head.next
