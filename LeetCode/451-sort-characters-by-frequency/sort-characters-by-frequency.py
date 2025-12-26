class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        result = ""
        
        for ch, freq in sorted(dic.items(), key=lambda x: x[1], reverse=True):
            result += ch * freq
        
        return result
