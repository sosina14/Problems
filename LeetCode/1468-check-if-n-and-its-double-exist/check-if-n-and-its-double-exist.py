class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        i = 0
        for num in arr:
            if num*2 in seen or (num%2== 0 and num//2 in seen):
                return True
            seen.add(num)
        return False 

        


        
        # 1st try but don't pass all test cases
        # arr1 = set(arr)
        # for i in range(len(arr)):
        #     x = arr[i]*2 
        #     if x in arr1:
        #         return True
        # return False 