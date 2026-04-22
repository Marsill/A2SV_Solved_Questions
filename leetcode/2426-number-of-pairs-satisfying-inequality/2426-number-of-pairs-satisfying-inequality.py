class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        A = [nums1[i] - nums2[i] for i in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, cnt1 = merge_sort(arr[:mid])
            right, cnt2 = merge_sort(arr[mid:])
            
            count = cnt1 + cnt2
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                count += len(right) - j
            
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
        
        return merge_sort(A)[1]