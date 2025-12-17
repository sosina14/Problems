class Solution:
    def averageValue(self, nums: List[int]) -> int:
        summ = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0 and nums[i] % 2 == 0:
                summ += nums[i]
                count += 1
        if count == 0:
            return 0
        else:
            average = int(summ/count)
            return average