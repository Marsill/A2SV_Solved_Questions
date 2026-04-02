class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        self.count = 0
        self.result = ""
        
        def backtrack(path):
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    self.result = path
                return
            
            for ch in letters:
                if not path or path[-1] != ch:
                    backtrack(path + ch)
                    if self.result:  
                        return
        
        backtrack("")
        return self.result