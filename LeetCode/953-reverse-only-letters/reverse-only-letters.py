class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s) 
        i=0
        j=len(arr)-1
        while i < j :
            if not arr[i].isalpha():
                i +=1
            elif not arr[j].isalpha():
                j -= 1
            else:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
        return "".join(arr)