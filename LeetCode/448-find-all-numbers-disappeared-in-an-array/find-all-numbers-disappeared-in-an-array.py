class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        numset = set(nums)
        for i in range(1,len(nums)+1):
            if i not in numset:
                arr.append(i)
        return arr