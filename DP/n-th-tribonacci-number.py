class Solution:
    def tribonacci(self, n: int) -> int:
        trib_array = [0,1,1]
        def recur(n):
            if n<len(trib_array):
                return trib_array[n]
            else:
                trib_array.append(recur(n-1)+recur(n-2)+recur(n-3))
            return trib_array[n]
        return recur(n)