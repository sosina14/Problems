class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxl = 0
        l = 0
        for i in s:
            while i in seen:
                seen.remove(s[l])
                l+=1
            seen.add(i)
            maxl = max(maxl , len(seen))
        return maxl
                