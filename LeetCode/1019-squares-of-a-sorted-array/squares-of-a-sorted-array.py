class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            x = i * i
            arr.append(x)
        arr.sort()
        return arr