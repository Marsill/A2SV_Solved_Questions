class Solution:
    def findRadius(self, ho: List[int], he: List[int]) -> int:
        ho.sort()
        he.sort()
        ans = float('-inf')
        he.append(float('inf'))
        for house in ho:
            idx = bisect_left(he, house)
            mine = float('inf')
            mine = min(mine, abs(house - he[idx]))
            if idx + 1 < len(he):
                mine = min(mine, abs(house - he[idx + 1]))
            if idx - 1 >= 0:
                mine = min(mine, abs(house - he[idx - 1]))
            ans = max(ans, mine)
        return ans