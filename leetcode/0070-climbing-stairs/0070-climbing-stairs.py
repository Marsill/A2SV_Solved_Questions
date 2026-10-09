class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        x = 1
        y = 2
        for i in range(2, n):
            x, y = y, x + y
        
        return y