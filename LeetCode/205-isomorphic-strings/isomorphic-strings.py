class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        seen1 = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 in seen and seen[c1] != c2) or (c2 in seen1 and seen1[c2]!= c1):
                return False
            seen[c1] = c2
            seen1[c2] = c1
        return True