class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        next_val = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= next_val:
                next_val = nums[i]
            else:
                k = math.ceil(nums[i] / next_val)
                ops += k - 1
                next_val = nums[i] // k

        return ops