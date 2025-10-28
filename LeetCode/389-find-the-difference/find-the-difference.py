class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return ch
            else:
                freq[ch] -= 1

        # list_s = list(s)
        # list_t = list(t)
        # seen = set()
        # for i in set(list_t):
        #     if i not in list_s:
        #         return i
        #     if i in seen:
        #         return i
        #     seen.add(i)