class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        def backtruck(i, curr_string):
            if len(curr_string) == len(digits):
                res.append(curr_string)
                return
            for c in digit_map[digits[i]]:
                backtruck(i + 1, curr_string + c)
        if digits:
            backtruck(0, '')
        return res