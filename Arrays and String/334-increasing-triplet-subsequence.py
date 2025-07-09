"""https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for el in nums:
            if el<=first:
                first= el
            elif el<=second:
                second= el
            else:
                return True
        return False 