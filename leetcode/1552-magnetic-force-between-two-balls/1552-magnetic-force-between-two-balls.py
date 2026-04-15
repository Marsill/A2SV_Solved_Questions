class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def countBalls(d):
            n_balls, cur = 1, position[0]
            for i in range(1, n):
                if position[i]-cur >= d:
                    n_balls += 1
                    cur = position[i]
            return n_balls
        
        l, r = 1, position[-1]-position[0]

        while l <= r:
            mid = (l+r)//2
            if countBalls(mid) >= m:
                l = mid+1
            else:
                r = mid-1
        return r