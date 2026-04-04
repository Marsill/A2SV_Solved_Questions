class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(w):
            yefejebign = 1
            cur = 0
            for num in weights:
                if num > w: return False
                cur += num
                if cur > w:
                    yefejebign += 1
                    cur = num
            return yefejebign <= days
        l = 1
        r = sum(weights)
        while l+1 < r:
            mid = (l+r)//2
            if checker(mid):
                r = mid
            else:
                l = mid
        return r
