class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        word = list(s)
        for i in range(0,len(word),2*k):
            j = i + k -1
            if j >= len(word):
                j = len(word)-1
            l = i
            r = j
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1

        return ''.join(word)

        #2nd method

        # word = list(s)
        # for i in range(0, len(word), 2*k):
        #     word[i:i+k] = reversed(word[i:i+k])
        # return ''.join(word)
