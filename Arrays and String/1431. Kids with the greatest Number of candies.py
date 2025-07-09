"""https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        bool_array=[]
        for el in candies:
            if el+extraCandies>=max_candies:
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array

        