"""https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def decodeString(self, s: str) -> str:
        temp_stack = []

        for ele in s:
            if ele!="]":
                temp_stack.append(ele)
            else:
                substr=""
                while temp_stack and temp_stack[-1]!="[":
                    substr=temp_stack.pop()+substr
                temp_stack.pop()
                int_k=""
                while temp_stack and temp_stack[-1].isdigit():
                    int_k=temp_stack.pop()+int_k
                temp_stack.append(int(int_k)*substr)
        return "".join(temp_stack)

                