class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # x = max(nums)
        # if len(nums) < 3:
        #     return x
        # y = set(nums)
        # for i in range(2):
        #     x = max(y)
        #     y.remove(x)
        # return max(y)

        
        y = set(nums) 
        if len(y) < 3:
            return max(y)
        for i in range(2):
            y.remove(max(y))
        return max(y)


