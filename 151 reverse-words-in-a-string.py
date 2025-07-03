class Solution:
    def reverseWords(self, s: str) -> str:
        final_output= []
        temp_array= []
        for ele in s:
            if not ele.isspace():
                temp_array.append(ele)
            elif temp_array:
                final_output.append("".join(temp_array))
                temp_array=[]
        if temp_array:
            final_output.append("".join(temp_array))
        # In another universe
        print(s.split())
        # final_output=s.split()
        # return " ".join(final_output[::-1])
        # both same
        return " ".join(final_output[::-1])
