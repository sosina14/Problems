class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = list(name)
        t = list(typed)
        i = 0 
        j = 0 
        while i < len(n) and j < len(t):
            if n[i] == t[j]:
                i += 1
                j += 1
            elif j > 0 and t[j] == t[j - 1]:  
                j += 1
            else:
                return False
        # If there are leftover characters in typed, they must be repeats of the last character
        while j < len(t):
            if t[j] != t[j - 1]:
                return False
            j += 1

        return i == len(n)
