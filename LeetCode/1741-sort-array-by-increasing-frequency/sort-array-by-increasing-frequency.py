class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def sort_n(n):
            return (count[n] , -n)
        nums.sort(key=sort_n)
        return nums
