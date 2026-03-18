class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n

        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1

        for i in range(1, n):
            freq[i] += freq[i-1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        MOD = 10**9 + 7
        total = 0
        for i in range(n):
            total = (total + nums[i] * freq[i]) % MOD

        return total