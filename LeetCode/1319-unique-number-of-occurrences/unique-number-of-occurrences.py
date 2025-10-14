class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        freqs = list(dic.values()) 
        if len(freqs) == len(set(freqs)):
            return True
        else:
            return False



           
        # arr.sort()
        # count = 1
        # for i in range(len(arr)-1):
        #     if arr[i] == arr [i+1]:
        #         count += 1
        #     else:
        #         count -= 1
        # if count == 0:
        #     return False
        # else:
        #     return True