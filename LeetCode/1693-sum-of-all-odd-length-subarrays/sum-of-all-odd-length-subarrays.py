class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        out = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1 , n+1):
                if (i+j)%2 != 0:
                    out += sum(arr[i:j])
        return out