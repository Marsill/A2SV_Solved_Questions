class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)
        
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [[None, None] for _ in range(bucket_count)]
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        max_gap = 0
        prev_max = min_val
        
        for b_min, b_max in buckets:
            if b_min is None:
                continue
            
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
        
        return max_gap