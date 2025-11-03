class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        arr = list(s)
        x = 0
        for i in range(len(arr) - 2): 
            count = 0
            if arr[i] != arr[i+1] and arr[i] != arr[i+2] and arr[i+1] != arr[i+2]:
                x += 1
        return x

        
# class Solution:
#     def countGoodSubstrings(self, s: str) -> int:
#         arr = list(s)
#         count = 0
#         x = 0
#         for i in range(len(arr)):
#             count = 0
#             for j in range(2):
#                 if arr[j] != arr[j+1]:
#                     count += 1
#                     if count == 3:
#                         x += 1
#         return x


