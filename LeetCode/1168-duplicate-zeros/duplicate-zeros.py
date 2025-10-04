class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x = len(arr)
        i=0
        while i < x:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 2
            else:
                i += 1
          
    
            
        