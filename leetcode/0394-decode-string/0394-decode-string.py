class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == ']':
                decode = ''
                while stack and stack[-1] != '[':
                    decode += stack.pop()
                stack.pop()
                
                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()

                

                encode = int(num[::-1]) * decode[::-1]
                for c in encode:
                    stack.append(c)
            else:
                stack.append(ch)
        return ''.join(stack)
