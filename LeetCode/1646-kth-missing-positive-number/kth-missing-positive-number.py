class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = []
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                seen.append(i)
        return seen[k-1]
        

