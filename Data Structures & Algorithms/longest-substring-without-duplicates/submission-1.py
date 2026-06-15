class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        check = set(s[0])
        max_length = 1
        for i in range(1, len(s)):
            while s[i] in check:
                check.remove(s[left])
                left += 1
            check.add(s[i])
            length = i - left + 1
            max_length = max(max_length, length)
        return max_length
        