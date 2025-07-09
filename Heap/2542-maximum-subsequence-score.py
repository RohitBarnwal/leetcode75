# https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75
from collections import defaultdict 
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairs.sort(key= lambda x:x[1], reverse=True)
        curr_sum = 0
        max_sum = 0
        heap = []
        for n1, n2 in pairs:
            curr_sum+=n1
            heapq.heappush(heap, n1)

            if len(heap)>k:
                removed = heapq.heappop(heap)
                curr_sum-=removed
            if len(heap)==k:
                max_sum = max(max_sum, curr_sum*n2)
        return max_sum