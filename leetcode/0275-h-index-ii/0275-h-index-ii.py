class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_max = 0
        for h in range(1, len(citations)+1):
            idx = bisect_left(citations, h)
            value = len(citations) - idx
            if value >= h:
                h_max = h
        return h_max
            
