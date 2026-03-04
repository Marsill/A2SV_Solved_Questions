class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]*len(nums)
        rem_dict = {0: -1}
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] + prefix[i-1]

            remainder = prefix[i] % k if k != 0 else prefix[i]
            
            if remainder in rem_dict:
                if i - rem_dict[remainder] > 1:
                    return True
            else:
                rem_dict[remainder] = i
        
        return False
        




      