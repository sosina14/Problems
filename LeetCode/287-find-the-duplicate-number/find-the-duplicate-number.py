class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i 
            seen.add(i)




        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i != j and nums[i] == nums[j]:
        #             count += 1
        #     if count >= 1:
        #         return nums[i]