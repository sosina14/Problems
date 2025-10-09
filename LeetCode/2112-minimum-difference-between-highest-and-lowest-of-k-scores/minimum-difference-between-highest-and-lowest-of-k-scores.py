class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_value = float('inf')
        for i in range(0,len(nums)-k +1):
            x = nums[i+k-1] - nums[i] 
            min_value = min(min_value , x)
        return min_value

        # nums.sort()
        # min_value = float('inf')
        # i = 0
        # j = len(nums)-1
        # if len(nums) == 1:
        #     return 0
        # while i < j:
        #     x = nums[j] - nums[i] 
        #     min_value = min(min_value , x)
        #     i += 1
        # return min_value

          