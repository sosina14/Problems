class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sorted_unique = sorted(set(arr))
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        result = [rank_map[num] for num in arr]
        return result
