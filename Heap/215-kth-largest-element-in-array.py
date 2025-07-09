# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i=1
        nums_n=[-el for el in nums ]
        heapq.heapify(nums_n)
        while i<k:
            heapq.heappop(nums_n)
            i+=1
        return -heapq.heappop(nums_n)
        