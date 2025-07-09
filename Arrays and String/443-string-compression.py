"""https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0

        while read<len(chars):
            count=0
            current_char = chars[read]
            while read<len(chars) and current_char==chars[read]:    
                read+=1
                count+=1
            chars[write]=current_char
            write+=1
            if count>1:
                for el in str(count):
                    chars[write]=el
                    write+=1
        return write