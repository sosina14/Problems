class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1 , n+1):
            arr.append(i)
        i = 0
        # x = math.ceil(n/2)
        while len(arr) > 1:
            i = (i + k-1) % len(arr)
            arr.pop(i)
        return arr[0]



        # Redeat Brihane's try but don't work
        # seen, i = set(), 1
        # while i < n + 1:
        #     curr = (i + k - 1) % n
        #     if curr not in seen:
        #         seen.add(curr)
        #         i = ((i + k - 1) % n ) + 1
        #         if i in seen:
        #             k += 1
        #             i = curr
        #             i = ((i + k - 1) % n ) + 1
        #     else:
        #         # seen.add(curr + 1)
        #         i += 1
        #     if len(seen) == n - 1:
        #         break

        # correct Answer
        # arr = deque()
        # for i in range(1 , n+1):
        #     arr.append(i)
        
        # while len(arr) > 1:
        #     for i in range(k-1):
        #         arr.append(arr.popleft())
        #     arr.popleft()
        
        # return arr[0]
            


