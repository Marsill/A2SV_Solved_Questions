class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_dict = defaultdict(int)
        res = []
        stack = []  #  [4]

        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                poped = stack.pop()
                if not stack:
                    res_dict[poped] = -1
                else:
                    res_dict[poped] = stack[-1]
            stack.append(num)
        while stack:
            poped = stack.pop()
            if not stack:
                res_dict[poped] = -1
            else:
                res_dict[poped] = stack[-1]
       
        for i, num in enumerate(nums1):
            if num in res_dict:
                res.append(res_dict[num])
        return res