# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):

        nums_dict = {}
        for el in nums:
            nums_dict[el] = nums_dict.get(el, 0) + 1
        count = 0
        for i, key in enumerate(nums_dict.keys()):
            nums[i] = key
            count +=1

        return len(nums[:count])


    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums)) # make changes in place, rather then creating new array 
        return len(nums)        

    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def removeDuplicates(self, nums):
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1

    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[j-1] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j


    def removeDuplicates(nums, k):
        if len(nums) <= k:
            return len(nums)

        i = k  # Start writing from index k

        for j in range(k, len(nums)):
            if nums[j] != nums[i - k]:
                nums[i] = nums[j]
                i += 1

        return i
