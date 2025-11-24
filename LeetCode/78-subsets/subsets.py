class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            new_sets = []
            for s in res:
                new_sets.append(s + [num])
            res += new_sets
        return res
