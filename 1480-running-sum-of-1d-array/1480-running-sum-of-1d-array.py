class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0
        prefix = []
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix.append(cur_sum)
        return prefix


