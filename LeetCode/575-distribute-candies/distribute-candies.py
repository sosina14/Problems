class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        x = int(len(candyType)/2)
        if len(set(candyType)) < x:
            return len(set(candyType))
        else:
            return x