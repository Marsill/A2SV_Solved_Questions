class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rem_dict = defaultdict(int)
        rem_dict[0] = 1

        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
                    
            count += rem_dict[diff]
            rem_dict[curr_sum] += 1

        return count

        