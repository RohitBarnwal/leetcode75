"""https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        final_output=[]
        for el1, el2 in zip(word1, word2):
            final_output.append(el1)
            final_output.append(el2)
        a= len(word1)
        b= len(word2)
        if a>b:
            final_output.extend(word1[b:])
        else:
            final_output.extend(word2[a:]) 
        return "".join(final_output)        