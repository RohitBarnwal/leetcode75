"""https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i,j=0,k
        
        current_sum = sum(nums[:j])
        max_sum= current_sum
        while j<len(nums):
            current_sum = current_sum- nums[i]+nums[j]
            j+=1
            i+=1
            max_sum=max(current_sum, max_sum)
        return max_sum/k
