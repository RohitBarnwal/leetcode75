"""https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = -1 # index with first occurance of 0
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                break
        if j!=-1:
            for i in range(j+1, len(nums)):
                if nums[i]!=0:
                    nums[j], nums[i]= nums[i], nums[j]
                    j+=1
            

