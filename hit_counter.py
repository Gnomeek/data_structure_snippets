"""
Design a hit counter which counts the number of hits received in the past $window seconds.

Your system should accept a timestamp parameter (in seconds granularity), and 
you may assume that calls are being made to the system in chronological order
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""
from collections import deque


class HitCounter:
    def __init__(self, window):
        self.window = window
        self.hits = []
        self.prefix_sum = []
    
    def hit(self, ts: int):
        self.hits.append(ts)

    def get_hits(self, ts: int) -> int:
        l = self.bisect_left(ts-self.window)
        return len(self.hits) - l

    def bisect_left(self, ts):
        l, r = 0, len(self.hits) - 1
        while l < r:
            mid = (l + r) >> 1
            if self.hits[mid] >= ts:
                r = mid
            else:
                l = mid + 1
        return l

class HitCounterWithQueue:
    def __init__(self, window):
        self.window = window
        self.hits = deque([])
    
    def hit(self, ts: int):
        self.hits.append(ts)

    def get_hits(self, ts: int) -> int:
        while self.hits and self.hits[0] <= ts - self.window:
            self.hits.popleft()
        return len(self.hits)


class HitCounterImproved:
    def __init__(self, window):
        self.window = window
        self.hit_cnt = []
        self.times = []
        self.prefix_sum = [0]
    
    def hit(self, ts: int):
        if self.times and self.times[-1] == ts:
            self.hit_cnt[-1] += 1
            self.prefix_sum[-1] += 1
        else:
            self.times.append(ts)
            self.hits.append(1)
            self.prefix_sum.append(self.prefix_sum[-1] + 1)

    def get_hits(self, ts: int) -> int:
        target = self.bisect_left(ts - self.window)
        return self.prefix_sum[-1] - self.prefix_sum[target]

    def bisect_left(self, ts):
        l, r = 0, len(self.hits) - 1
        while l < r:
            mid = (l + r) >> 1
            if self.hits[mid] >= ts:
                r = mid
            else:
                l = mid + 1
        return l