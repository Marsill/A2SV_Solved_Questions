class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if num == 0:
                return 1
            
            half = power(n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
            
        if n < 0:
            x = 1/ x
            n = -n
        return pow(x, n)