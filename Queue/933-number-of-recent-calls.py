class RecentCounter:

    def __init__(self):
        self.queue=deque()
        self.count=0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count+=1
        while self.queue and self.queue[0]<t-3000:
            self.count-=1
            self.queue.popleft()
        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)