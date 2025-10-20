class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        runningsum = 0
        for i in nums:
            runningsum += i
            arr.append(runningsum)
        return arr


        # arr = []
        # sm = 0
        # for i in range(len(nums)):
        #     sm += nums[i] 
        #     arr.append(sm)
        # return arr