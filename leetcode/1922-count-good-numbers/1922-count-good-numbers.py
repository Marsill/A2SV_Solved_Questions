class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        return (power(5, even_positions) * power(4, odd_positions)) % MOD