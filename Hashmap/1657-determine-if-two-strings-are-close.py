"""https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        word_dict1= Counter(word1)
        word_dict2= Counter(word2)

        return sorted(word_dict1.values())==sorted(word_dict2.values()) and set(word1)==set(word2)