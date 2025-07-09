"""https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        count_zeros=0
        max_len=0
        while j<len(nums):
            if nums[j]==0:
                count_zeros+=1
            if count_zeros>k:
                if nums[i]==0:
                    count_zeros-=1
                i+=1
            max_len=max(max_len, j-i+1)
            j+=1
        return max_len