class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) -1):
            summ = nums[i] + nums[i+1]
            if summ in seen:
                return True
            seen.add(summ)
        return False