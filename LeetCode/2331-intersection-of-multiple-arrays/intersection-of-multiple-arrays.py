class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = {} 
        for sublist in nums:      
            for num in sublist:   
                count[num] = count.get(num, 0) + 1
        result = [num for num, freq in count.items() if freq == len(nums)]
        return sorted(result)
        
        # arr = []
        # seen = {}
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i],[j] in seen:
        #             arr.append(nums[i],[j])
        #         seen[nums[i]] = i
        # return arr





