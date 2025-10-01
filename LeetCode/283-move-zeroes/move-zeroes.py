class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j] , nums[i]
                i += 1
            j += 1
















        w = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                # t = nums[r]
                # nums[r] = nums[w]
                # nums[w] = t
                nums[r] , nums[w] = nums[w], nums[r]
                w += 1
            r += 1 
        
# r = 1
# w = 0
# 1,0,0,3,12
# r = 2
# w = 1
# no change r = 3
# w = 1
# 1,3,0,0,12
# w = 2
# r = 4
# 1,3,12,0,0


        # write = 0
        # read = 0
        # while read < len(nums):
        #     if nums[read] != 0:
        #         temp = nums[read]
        #         nums[read] = nums[write]
        #         nums[write] = temp
        #         write = write + 1
        #     read = read + 1
















