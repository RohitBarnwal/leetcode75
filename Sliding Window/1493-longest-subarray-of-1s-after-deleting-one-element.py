"""https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i,j=0,0
        count_zero=0

        max_len=0
        while j<len(nums):
            if nums[j]==0:
                count_zero+=1

            if count_zero>1:
                if nums[i]==0:
                    count_zero-=1
                i+=1
            max_len=max(max_len, j-i+1)
            j+=1
        return max_len-1
        