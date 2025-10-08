class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False


        #Time Limit Exceeded answer of me
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and abs(i-j)<=k and i!=j:
        #             return True
        # return False
                    
                