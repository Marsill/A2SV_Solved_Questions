class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)

        fenwick = Fenwick(max_val)
        cost = 0

        for i, x in enumerate(instructions):
            less = fenwick.query(x - 1)
            greater = i - fenwick.query(x)

            cost += min(less, greater)
            cost %= MOD

            fenwick.update(x, 1)

        return cost

class Fenwick:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

