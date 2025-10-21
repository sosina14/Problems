class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = {0: 1} 

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count

        # count = 0
        # for start in range(len(nums)):
        #     summ = 0
        #     for end in range(start, len(nums)):
        #         summ += nums[end]
        #         if summ == k:
        #             count += 1
        # return count



        # summ = 0
        # arr = []
        # for i in range(len(nums)):
        #     summ += nums[i]
        #     arr.append(nums[i])
        #     if summ == k:
        #         return len(arr)