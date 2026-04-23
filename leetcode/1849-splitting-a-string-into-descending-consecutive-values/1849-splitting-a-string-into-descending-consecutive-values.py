class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(index, prev, count):
            if index == n:
                return count >= 2 
            
            num = 0
            for i in range(index, n):
                num = num * 10 + int(s[i])
                
                if prev is None:
                    if dfs(i + 1, num, count + 1):
                        return True
                else:
                    if num == prev - 1:
                        if dfs(i + 1, num, count + 1):
                            return True
                    elif num >= prev:
                        break  
            
            return False
        
        return dfs(0, None, 0)