"""https://leetcode.com/problems/find-pivot-index?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if right_sum==left_sum:
                return i
            left_sum = left_sum+num
        return -1
        # i=0
        # while i<len(nums):
        #     sum_l = sum(nums[:i])
        #     sum_r = sum(nums[i+1:])
        #     if sum_l==sum_r:
        #         return i    
        #     i+=1
        # return -1    