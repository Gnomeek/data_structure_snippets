import random
from typing import List


class RandomIntWithWeight:

    def __init__(self, w: List[int]):
        self.weight = w
        self.prefix_sum = [0]
        self.total = 0
        for weight in w:
            self.prefix_sum.append(self.prefix_sum[-1] + weight)
            self.total += weight
        

    def pickIndex(self) -> int:
        seed = random.randint(1, self.total)
        l, r = 1, len(self.prefix_sum) - 1
        while l < r:
            mid = (l + r) >> 1
            if self.prefix_sum[mid] >= seed:
                r = mid
            else:
                l = mid + 1
        return l - 1
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()