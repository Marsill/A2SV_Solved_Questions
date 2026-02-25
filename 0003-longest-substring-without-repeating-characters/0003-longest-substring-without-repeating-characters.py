class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        left = 0
        max_count = 0
        for right in range(len(s)):
            while s[right] in set_s:
                set_s.remove(s[left])
                left += 1
            
            set_s.add(s[right])
            max_count = max(max_count, len(set_s))
        return max_count