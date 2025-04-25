class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        max_avg = max_sum/k

        for i in range(k,len(nums)):
            max_sum += nums[i]
            max_sum -= nums[i-k]
            max_avg = max(max_avg,max_sum/k)

        return max_avg



