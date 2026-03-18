class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        stepSum = 0
        for i in nums:
            stepSum += i
            prefix.append(stepSum)
        
        if min(prefix) < 0:
            result = 1 - min(prefix)
        else:
            return 1
        return result