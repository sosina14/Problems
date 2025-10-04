class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = ['a', 'e','i','o','u','A','E','I','O','U']
        word = list(s)
        i = 0
        j = len(word)-1
        while i < j:
            if word[i] not in arr:
                i += 1
                continue
            if word[j] not in arr:
                j -= 1
                continue
            if word[i] in arr and word[j] in arr:
                word[i],word[j] = word[j],word[i]
                i += 1
                j -= 1
        return ''.join(word)