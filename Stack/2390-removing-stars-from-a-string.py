"""https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def removeStars(self, s: str) -> str:
        
        ans=[]
        for el in s:
            if el=="*":
                ans.pop()
            else:
                ans.append(el)
        return "".join(ans)

