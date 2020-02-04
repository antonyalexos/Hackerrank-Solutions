"""
    Delete duplicate nodes
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the head of the linked list in the below method.
    """

def RemoveDuplicates(head):
    
    comp=head
    initial_head=head
    
    if(head!=None):
        head=head.next
    
    while(head!=None):
        if(head.data==comp.data):
            comp.next=head.next
        else:
            comp=head
        head=comp.next
    
    return initial_head