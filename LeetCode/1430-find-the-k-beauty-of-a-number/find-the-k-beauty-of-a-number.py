class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        i=0
        numm = str(num)
        if len(numm) == 1:
            return 1
        while i < len(numm)-k+1:
            y = int(numm[i:i+k])
            if y != 0 and num % y  == 0:
                count+=1
                i+=1
            else:
                i+=1
        return count