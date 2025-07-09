"""https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        element_dict = {}
        operations=0
        for ele in nums:
            compliment = k-ele
            if element_dict.get(compliment):
                element_dict[compliment]-=1
                operations+=1
            else:
                element_dict[ele] = element_dict.get(ele,0) + 1
        return operations