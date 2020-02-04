"""
    Merge two linked lists
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the head of the linked list in the below method.
    """
def MergeLists(headA, headB):
    new = Node()
    final = Node()
    if(headA!=None and headB!=None):
        if(headA.data>=headB.data):
            new = Node(headB.data,None)
            final = new
            headB = headB.next
        else:
            new = Node(headA.data, None)
            final = new
            headA = headA.next
    elif(headB==None and headA!=None):
        new = Node(headA.data,None)
        final = new
        headA = headA.next
    elif(headA==None and headB!=None):
        new = Node(headB.data,None)
        final = new
        headB = headB.next
    while(headA!=None and headB!=None):
        if(headA.data>=headB.data):
            new.next = headB
            headB = headB.next
        else:
            new.next = headA
            headA = headA.next
        new = new.next
    while(headB==None and headA!=None):
        new.next = headA
            headA = headA.next
while(headA==None and headB!=None):
    new.next = headB
        headB = headB.next
    return final