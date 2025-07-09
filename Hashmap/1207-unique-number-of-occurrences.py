"""https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75"""
from collections import Counter 

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums_dict = Counter(arr)
        nums_set = set(nums_dict.values())
        return len(nums_dict.values())==len(nums_set)
        