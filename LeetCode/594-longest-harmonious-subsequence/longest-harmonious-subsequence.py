class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maxlen = 0
        j = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxlen = max(maxlen, i-j+1)
        return maxlen