class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        time = 0
        target = tickets[k]
        
        for round_num in range(target - 1):
            for i in range(n):
                if tickets[i] > round_num:
                    time += 1
   
        for i in range(k + 1):
            if tickets[i] >= target:
                time += 1
        
        return time