class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        maxlen = 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                j += 1
            else:
                maxlen = max(maxlen , j)
                j = 1
        return max(maxlen,j)

        # i = 0
        # j = 0
        # maxlen = 0
        # while j - i < 1:
        #     j += 1
        #     if nums[j] - nums[i] == 1:
        #         maxlen = max(maxlen , j + 1)
        #         i += 1
        #     else:
        #         break
        # return maxlen
