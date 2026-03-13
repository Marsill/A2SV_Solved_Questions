class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = deque()
        res = []

        for i in range(k):
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[i])
   
        res.append(max_q[0])
        l = 0

        for r in range(k, len(nums)):           
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[r])
            if max_q[0] == nums[l]:
                max_q.popleft()
            l += 1
            res.append(max_q[0])

        return res
            