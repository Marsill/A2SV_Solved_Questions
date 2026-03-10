class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0]*len(nums)
        rem_dict = {0: 1}
        count = 0
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] + prefix[i-1]

            remainder = prefix[i] % k if k != 0 else prefix[i]
            
            if remainder in rem_dict:
                count += rem_dict[remainder]

            rem_dict[remainder] = rem_dict.get(remainder, 0)+1

        return count
        




      
        