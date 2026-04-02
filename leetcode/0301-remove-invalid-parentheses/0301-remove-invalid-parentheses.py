class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = self.min_removals(s)
        res = set()

        def dfs(index, path, left_rem, right_rem, open_paren):
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and open_paren == 0:
                    res.add(path)
                return

            char = s[index]

            if char == '(':
                if left_rem > 0:
                    dfs(index + 1, path, left_rem - 1, right_rem, open_paren)
                dfs(index + 1, path + char, left_rem, right_rem, open_paren + 1)

            elif char == ')':
                if right_rem > 0:
                    dfs(index + 1, path, left_rem, right_rem - 1, open_paren)
                if open_paren > 0:
                    dfs(index + 1, path + char, left_rem, right_rem, open_paren - 1)

            else:
                dfs(index + 1, path + char, left_rem, right_rem, open_paren)

        dfs(0, "", left, right, 0)
        return list(res)

    def min_removals(self, s):
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right