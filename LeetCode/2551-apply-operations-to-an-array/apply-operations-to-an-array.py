class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        r = 0
        w = 1      
        while w < len(nums):
            if nums[r] == 0 and nums[w] != 0:
                nums[r],nums[w] = nums[w],nums[r]
                r += 1
                w += 1
            elif nums[r] != 0:
                w += 1
                r += 1
            else:
                w += 1
        return nums









        # i = 0
        # j = 1
        # while j < len(nums):
        #     if nums[i] == nums[j]:
        #         nums[i] *= 2
        #         nums[j] = 0
        #         i += 1
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1
        
        # n = []
        # z = []
        # for num in nums:
        #     if num == 0:
        #         z.append(0)
        #     else:
        #         n.append(num)
        # return n + z
