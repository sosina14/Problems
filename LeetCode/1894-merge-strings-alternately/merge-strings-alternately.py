class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        i , j = 0 , 0
        while i < len(word1) and i < len(word2):
            arr.append(word1[i])
            arr.append(word2[i])
            i += 1
            j += 1
        arr.append(word1[i:])
        arr.append(word2[j:])
        return "".join(arr)
       
            
