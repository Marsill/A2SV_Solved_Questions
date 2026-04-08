class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans, res = -1, -1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
            
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] < target: 
                
                l = mid + 1
            else:
                res = mid
                r = mid - 1
       
        if nums and  nums[res] != target and nums[ans] != target:
            return [-1, -1]
        return [res, ans]
    