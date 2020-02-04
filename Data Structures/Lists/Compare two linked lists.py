#Body
"""
    Compare two linked list
    head could be None as well for empty list
    Node is defined as
    
    class Node(object):
    
    def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node
    
    return back the head of the linked list in the below method.
    """

def CompareLists(headA, headB):
    while(headA!=None and headB!=None and headA.data==headB.data):
        if(headA.next==None and headB.next==None):
            return 1
        elif(headA.data!=headB.data):
            return 0
        headA = headA.next
        headB = headB.next
    return 0

"""
def CompareLists(headA, headB):
    while(1):
        if(((headA == None)^(headB == None)) == 1 ):
            return 0
        else:
            if(headA == None and headB == None):
                return 1
            if(headA.data != headB.data):
                return 0
            else:
                headA = headA.next
                headB = headB.next
"""