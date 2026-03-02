class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.result = []
        

    def sumRange(self, left: int, right: int) -> int:
        self.curr_sum = 0
        for i in range(left, right+1):
            self.curr_sum += self.nums[i]
        return self.curr_sum
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)