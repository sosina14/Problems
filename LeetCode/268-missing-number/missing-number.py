class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        #0,1,3
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
            