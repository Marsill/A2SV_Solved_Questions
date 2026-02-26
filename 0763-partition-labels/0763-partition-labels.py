class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        appear = {}
        res = []
        active = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in appear:
                active += 1
            appear[s[i]] = appear.get(s[i], 0) + 1

            if count[s[i]] == appear[s[i]]:
                active -= 1
            if active == 0:
                res.append(i - start + 1)
                start = i + 1
        return res