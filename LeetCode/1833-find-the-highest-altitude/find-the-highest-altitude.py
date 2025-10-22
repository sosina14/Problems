class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            arr = [0]
            pre = 0

            for i in gain:
                pre += i
                arr.append(pre)
            return max(arr)