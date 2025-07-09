# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll_array = []
        while head:
            ll_array.append(head.val)
            head=head.next
        max_sum=0
        length = len(ll_array)

        for i in range(0,(length // 2)):
            local_max = ll_array[i]+ll_array[length-1-i]
            max_sum = max(max_sum, local_max)
        
        return max_sum

        