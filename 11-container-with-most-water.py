"""https://leetcode.com/problems/container-with-most-water/submissions/1665826795/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        l = 0
        r = len(heights)-1    
        while l<r:
            area = min(heights[l], heights[r])*(r-l)
            max_area = max(max_area, area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return max_area