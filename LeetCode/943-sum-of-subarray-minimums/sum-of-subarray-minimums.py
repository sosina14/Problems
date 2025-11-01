# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         n = len(arr)
#         summ = 0
#         MOD = 10**9 + 7 
#         for i in range(n):
#             curr_min = arr[i]
#             for j in range(i,n):
#                 curr_min = min(curr_min,arr[j])
#                 summ += curr_min
#                 summ %= MOD 
#         return summ


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        stack = []
        left = [0] * n
        right = [0] * n
        
        # 1️⃣ Calculate how many elements are greater on the left
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))
        
        stack = []
        # 2️⃣ Calculate how many elements are >= on the right
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))
        
        # 3️⃣ Combine contributions
        total = 0
        for i in range(n):
            total += arr[i] * left[i] * right[i]
            total %= MOD
        
        return total

