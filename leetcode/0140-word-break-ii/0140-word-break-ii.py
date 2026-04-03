class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        curr = []
        def backtruck(i):
            if i == len(s):
                res.append(' '.join(curr))
                return
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    curr.append(w)
                    backtruck(j+1)
                    curr.pop()

        backtruck(0)
        return res