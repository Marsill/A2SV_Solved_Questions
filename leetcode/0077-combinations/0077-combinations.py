class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtruck(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return
            
            for c in range(start, n + 1):
                comb.append(c)
                backtruck(c+1, comb)
                comb.pop()
        backtruck(1, [])
        return ans