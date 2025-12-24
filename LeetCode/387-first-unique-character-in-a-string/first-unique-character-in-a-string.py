class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = list(s)
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key in dic:
            if dic[key] == 1:
                return arr.index(key)
        return -1
