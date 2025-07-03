class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while i < len(flowerbed):
            can_place = False
            if flowerbed[i] == 0:
                left_empty = (i==0 or flowerbed[i-1]==0)
                right_empty = (i==len(flowerbed)-1 or flowerbed[i+1]==0) 

                if left_empty and right_empty:
                    can_place = True
            if can_place:
                flowerbed[i]=1
                n-=1
                i+=2
            else:
                i+=1
            if n==0:
                return True
        return n<=0
