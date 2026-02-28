class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = defaultdict(int)
            left = 0
            subarray = 0

            for right in range(len(nums)):
                count[nums[right]] += 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                subarray += right - left + 1

            return subarray

        return atMost(k) - atMost(k-1)