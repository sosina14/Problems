class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) -1):
            arr_sum = nums[i] + nums[i+1]
            if arr_sum in seen:
                return True
            seen.add(arr_sum)
        return False