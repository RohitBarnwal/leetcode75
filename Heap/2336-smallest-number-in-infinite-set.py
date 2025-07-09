# https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.maintain_smallest_num = []
        self.nums_removed_set = set()
    
    def popSmallest(self):

        if self.maintain_smallest_num:
            smallest_num = heapq.heappop(self.maintain_smallest_num)
            self.nums_removed_set.remove(smallest_num)
            return smallest_num
        else:
            self.smallest+=1
            return self.smallest-1
    
    def addBack(self, num):
        if num<self.smallest and num not in self.nums_removed_set:
            self.nums_removed_set.add(num)
            heapq.heappush(self.maintain_smallest_num, num)
    