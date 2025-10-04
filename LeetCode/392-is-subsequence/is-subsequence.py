class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = list(t)
        arr1 = list(s)
        count = 0
        j = 0
        for i in range(len(arr1)):
            while j < len(arr) and arr1[i] != arr[j]:
                j += 1
            if j == len(arr):  
                break
            count += 1
            j += 1 
        if count == len(arr1):
            return True 
        else:
            return False
            
