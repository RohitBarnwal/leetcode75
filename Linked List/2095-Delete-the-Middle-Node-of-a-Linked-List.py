# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next
        mid=n//2
        count=0
        curr1=head
        if mid==0:
            return head.next
        while count<mid-1 and curr1:
            count+=1
            curr1=curr1.next
        if curr1.next:
            curr1.next=curr1.next.next
        return head

    
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return None

#         slow = head
#         fast = head
#         prev = None

#         while fast and fast.next:
#             fast = fast.next.next
#             prev = slow
#             slow = slow.next

#         # delete middle node
#         prev.next = slow.next
#         return head
