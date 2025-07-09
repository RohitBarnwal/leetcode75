# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        curr = head
        even_head = ListNode() 
        even = even_head
        odd = head
        while curr and curr.next:
            even.next=curr.next 
            even=even.next
            curr.next = curr.next.next
            odd = curr 
            curr = curr.next
        even.next = None 
        if curr:
            curr.next = even_head.next
        else:
            odd.next = even_head.next
        return head 

        
 
