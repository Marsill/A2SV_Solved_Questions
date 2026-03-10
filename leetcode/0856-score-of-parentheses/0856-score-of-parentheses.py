class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        var = 0

        for i in range(len(s)):
            count = 0
            if s[i] == '(':
                stack.append(s[i])
            else:
                while stack[-1] != '(':
                    count += stack[-1]
                    stack.pop()
                stack.pop()

                if count > 0:
                    count = count * 2
                else:
                    count = 1
                stack.append(count)

        return sum(stack)