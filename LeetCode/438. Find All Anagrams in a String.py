class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        arr = []
        window = defaultdict(int)
        target = defaultdict(int)
        
        if len(p) > len(s):
            return []

        for char in p:
            target[char] += 1
        for i in range(k):
            window[s[i]] += 1
        if window == target:
            arr.append(0)
        for i in range(k,len(s)):
            window[s[i]] += 1
            window[s[i-k]] -= 1
            if window[s[i-k]] == 0:
                del window[s[i-k]]
            if window == target:
                arr.append(i-k +1)
        return arr
    
                
             


        
