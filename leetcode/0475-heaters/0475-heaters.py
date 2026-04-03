class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            ans = len(arr)  
            
            while left <= right:
                mid = (left + right) // 2
                
                if arr[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return ans
        
        radius = 0
        
        for house in houses:
            i = binary_search(heaters, house)
            
            left_dist = float('inf')
            if i - 1 >= 0:
                left_dist = house - heaters[i - 1]
            
            right_dist = float('inf')
            if i < len(heaters):
                right_dist = heaters[i] - house
            
            closest = min(left_dist, right_dist)
            radius = max(radius, closest)
        
        return radius