class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}   # char -> last seen index
        left = 0
        res = 0

        for right, ch in enumerate(s):
            # if char seen inside current window
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            last_index[ch] = right
            res = max(res, right - left + 1)

        return res
