class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)            
        
        if ch not in arr:
            return word              
        
        idx = arr.index(ch)       
        
        prefix = arr[:idx + 1]      
        prefix.reverse()            
        
        rest = arr[idx + 1:]          
        
        return "".join(prefix + rest) 
