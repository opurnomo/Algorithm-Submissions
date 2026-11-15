class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        H = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in H:
                l = max(H[s[r]] + 1, l)
            H[s[r]] = r
            res = max(res, r - l + 1)
        return res