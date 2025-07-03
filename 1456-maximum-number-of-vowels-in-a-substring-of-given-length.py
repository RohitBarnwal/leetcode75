"""https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i,j=0,k
        vowels=set("aeiou")

        subs=s[i:j]
        max_count=0
        count=0
        for el in subs:
            if el in vowels:
                count+=1
        max_count = count
        while j<len(s):
            if s[i] in vowels:
                count-=1
            if s[j] in vowels:
                count+=1
            max_count= max(max_count, count)
            j+=1
            i+=1
        return max_count