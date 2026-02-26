class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
                
        count = {}
        max_sum = 0
        left = 0
        if 0 not in nums:
            return len(nums) - 1

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count.get(0, 0) > 1:
                count[nums[left]] -= 1
                left += 1
            max_sum = max(max_sum, (right - left + 1)- count.get(0, 0))

        return max_sum







        