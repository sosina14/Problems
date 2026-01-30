class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seen= s.split()
        return len(seen[-1])
        