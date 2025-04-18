class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr =[]
        for i in range(1, n + 1):
            arr.append(i)
        
        start = 0
        while len(arr) > 1:
            start = (start + k-1) % len(arr)
            arr.pop(start)
        return arr[0]


