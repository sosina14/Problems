class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):
            summ = nums[i]
            for j in range(i+1,n):
                if nums[j] > nums[j-1]:
                    summ += nums[j]
                else:
                    break
            max_sum = max(max_sum, summ)
        return max_sum

