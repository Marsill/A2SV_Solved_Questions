class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        result = []

        for l, r, direction in shifts:
            if direction == 1:
                prefix[l] += 1
                if r+1 < len(s):
                    prefix[r+1] -= 1
            else:
                prefix[l] -= 1
                if r+1 < len(s):
                    prefix[r+1] += 1

        r = 0
        for i, ch in enumerate(s):
            r += prefix[i]
            new_char = chr((ord(ch) - ord('a') + r) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)