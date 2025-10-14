class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        count = 0
        max_index = nums.index(x)
        for i in range(len(nums)):
            if i != max_index and x >= 2 * nums[i]: 
                count += 1
        if count == len(nums)-1:
            return max_index
        else:
            return -1