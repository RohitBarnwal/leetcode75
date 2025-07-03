"""https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_sum = 1
        output_array = [1]*len(nums)

        for i in range(len(nums)):
            output_array[i]= prefix_sum
            prefix_sum*=nums[i]
        suffix_sum = 1
        
        for i in range(len(nums)-1,-1,-1):
            output_array[i]*= suffix_sum
            suffix_sum*=nums[i] 
        return output_array

        # total_product = 1
        # zero_count = 0

        # # Step 1: Calculate product of all non-zero elements
        # for num in nums:
        #     if num != 0:
        #         total_product *= num
        #     else:
        #         zero_count += 1

        # # Step 2: Handle different zero cases
        # if zero_count > 1:
        #     return [0] * len(nums)
        
        # if zero_count == 1:
        #     return [total_product if num == 0 else 0 for num in nums]

        # # Step 3: No zeros — divide total_product by each element
        # return [total_product // num for num in nums]
