"""
    Insert a node into a sorted doubly linked list
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None, prev_node = None):
    self.data = data
    self.next = next_node
    self.prev = prev_node
    
    return the head node of the updated list
    """

def SortedInsert(head, data):
    temp = head
    new_node = Node(data)
    if temp == None:
        return new_node
    else:
        while temp.next != None and temp.next.data < data:
            temp = temp.next
    new_node.prev=temp
    new_node.next=temp.next
    temp.next=new_node
    return head