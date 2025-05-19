#  Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr.append(arr1[j])
        i = 0
        arrnew=[]
        while i < len(arr1) or i < len(arr2):
            if arr1[i] in arr2:
                i+=1
            else:
                arrnew.append(arr1[i])
                i += 1
        arrnew.sort()
        for i in arrnew:
            arr.append(i)
        return arr
