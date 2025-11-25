class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        arr = []
        for i in nums:
            if i in seen:
                arr.append(i)
            else:
                seen.add(i)
        return arr