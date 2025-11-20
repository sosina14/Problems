# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         i = 0
#         j = 0
#         summ = 0
#         max_sum = nums[0]
#         n = len(nums)
#         while j < n:
#             summ += nums[j]
#             max_sum = max(max_sum, summ)
#             while summ < 0 and i <= j:
#                 summ -= nums[i]
#                 i += 1
#             j += 1

#         return max_sum



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
