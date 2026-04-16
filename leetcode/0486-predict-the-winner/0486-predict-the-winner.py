class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right):
            if left == right:
                return nums[left]
            
            diff1 = nums[left] - play(left + 1, right)
            diff2 = nums[right] - play(left, right-1)

            return max(diff1, diff2)
        return play(0, len(nums)-1) >= 0