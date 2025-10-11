class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(x for x in nums if nums.count(x) == 1)
        
        # nums.sort()
        # summ = 0
        # # [1,2,2,3]
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         i += 2
        #     else:
        #         summ += nums[i]
        #         i += 1
        # return summ