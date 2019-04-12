import copy
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # If only one element, so removing that element.
        if(head.next==None):
            return None
        
        # points to the tail-n location
        pointer1=head
        
        # points to the tail 
        pointer2=copy.copy(head)
        
        for i in range(n):
            pointer2=pointer2.next
        
        # if we have to remove the first node
        if(pointer2==None):
            # The pointer will be none only if it has reached the end
            # If it has reached the end, then the element to be removed it the first element
            head=head.next
            return head
        
        # If the number of nodes in the linked list is more than n
        while(pointer2.next):
            pointer1=pointer1.next
            pointer2=pointer2.next
         
        # If we have to remove the last node
        if(n==1):
            pointer1.next=None
        else:
            pointer1.next=pointer1.next.next
        
        return(head)


obj1=ListNode(1)
obj2=ListNode(2)
obj1.next=obj2
n=1
sol=Solution()
root=sol.removeNthFromEnd(obj1, n)