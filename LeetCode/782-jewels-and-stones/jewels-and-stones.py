class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in range(len(stones)):
            if stones[j] in jewels:
                count += 1
        return count
           
