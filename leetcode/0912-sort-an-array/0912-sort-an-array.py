class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(l, r, nums):
            if l == r:
                return [nums[l]]
            
            mid = (l+r)//2
            
            left = mergesort(l, mid, nums) #[2,5]
            right = mergesort(mid+1, r, nums)

            return merge(left, right)

        def merge(left, right):
            u = 0
            d = 0
            res = []

            while u < len(left) and d < len(right):
                if left[u] <= right[d]:
                    res.append(left[u])
                    u += 1
                else:
                    res.append(right[d])
                    d += 1
            
            res.extend(left[u:])
            res.extend(right[d:])
            return res

        return mergesort(0, len(nums)-1, nums)