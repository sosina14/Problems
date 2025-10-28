class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        arr1 = []
        for i in nums:
            if i % 2 == 0:
                arr.append(i)
            else:
                arr1.append(i)
        for j in arr1:
            arr.append(j)
        return arr