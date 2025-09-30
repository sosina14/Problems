class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                t = nums[r]
                nums[r] = nums[w]
                nums[w] = t
                w += 1
            r += 1 

        # write = 0
        # read = 0
        # while read < len(nums):
        #     if nums[read] != 0:
        #         temp = nums[read]
        #         nums[read] = nums[write]
        #         nums[write] = temp
        #         write = write + 1
        #     read = read + 1
















