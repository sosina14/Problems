class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        # print(arr)
        new = []
        for i in arr:
            x = i[::-1]
            new.append(x)
        return " ".join(new)