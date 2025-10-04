class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        r = word[::-1]
        return ' '.join(r)