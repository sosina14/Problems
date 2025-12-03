class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque()
        maxl = 0
        for i in s:
            while i in seen:
                seen.popleft()
            seen.append(i)
            maxl = max(maxl , len(seen))
        return maxl
                