class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        x = [set(x) for x in responses]
        d = Counter(val for f in x for val in f)

        max_value = max(d.values())

        c = [key for key, values in d.items() if values == max_value]
        return min(c)


