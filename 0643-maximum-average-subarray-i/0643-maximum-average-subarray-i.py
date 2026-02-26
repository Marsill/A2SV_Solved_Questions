class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        max_sum = float('-inf')
        
        for i in range(k):
            window += nums[i]
        
        max_sum = window
        left = 0
        for right in range(k, len(nums)):
            window += nums[right]
            window -= nums[left]

            max_sum = max(max_sum, window)
            left += 1
        return max_sum/k
