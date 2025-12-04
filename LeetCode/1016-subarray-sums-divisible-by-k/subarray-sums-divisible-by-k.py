class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            pref += num
            r = pref % k

            count += freq.get(r, 0)
            freq[r] = freq.get(r, 0) + 1

        return count

# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i , len(nums)):
        #         summ = sum(nums[i:j+1])
        #         if summ % k == 0:
        #             count += 1
        # return count 