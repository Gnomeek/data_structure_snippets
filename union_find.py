class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = size
        self.rank = [1] * size
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        if self.rank[a] >= self.rank[b]:
            self.parent[b] = a
            self.rank[a] += self.rank[b]
        else:
            self.parent[a] = b
            self.rank[b] += self.rank[a]
        return True
    
    def group_size(self):
        res = {}
        for i in range(self.size):
            parent = self.find(i)
            res[parent] = self.rank[parent]
        return res
