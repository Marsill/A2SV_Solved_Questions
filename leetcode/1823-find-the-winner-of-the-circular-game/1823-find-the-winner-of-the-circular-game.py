class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def game(n):
            if n == 1:
                return 0
            return (game(n - 1) + k) % n
        
        return game(n) + 1