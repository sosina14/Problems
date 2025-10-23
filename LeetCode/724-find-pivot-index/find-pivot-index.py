class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)      
        leftSum = 0            

        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]   
            if leftSum == rightSum:                
                return i                          
            leftSum += nums[i]                    
        return -1                                 

        # i = 0
        # j = len(nums)-1
        # isum = 0
        # jsum = 0
        # while i < j:
        #     isum += nums[i]
        #     jsum += nums[j]
        #     if isum == jsum:
        #         return nums[i+1]
        #     i += 1
        #     j -= 1
        