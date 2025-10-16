class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = list(ransomNote)
        m = list(magazine)
        seen = {}
        for i in m:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for j in n:
            if j not in seen or seen[j] == 0:
                return False
            seen[j] -= 1
         
        return True
        
      
           