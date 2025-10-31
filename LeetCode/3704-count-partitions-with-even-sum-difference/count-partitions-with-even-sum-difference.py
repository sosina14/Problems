class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        arr = []
        count = 0
        sumn = sum(nums)
        for i in range(len(nums)-1):
            arr.append(nums[i])
            sumn -= nums[i]
            if abs(sum(arr) - sumn) % 2 == 0:
                count += 1
        return count