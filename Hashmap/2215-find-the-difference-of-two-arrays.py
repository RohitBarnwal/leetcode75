"""https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1670564610/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        intersections = set(nums1) & set(nums2)
        
        return [list(set(nums1)-intersections), list(set(nums2)-intersections)]

