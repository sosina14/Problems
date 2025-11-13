class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}                   
        for i in range(len(s)):
            last[s[i]] = i            
        result = []                  
        used = set()                  
        for i in range(len(s)):
            ch = s[i]
            if ch not in used:
                while result and result[-1] > ch and last[result[-1]] > i:
                    used.remove(result[-1])   
                    result.pop()             
                result.append(ch)
                used.add(ch)
        return "".join(result)


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         seen = []                  # stack-like list
#         in_seen = set()            # faster lookup
#         last_occurrence = {c: i for i, c in enumerate(s)}  # last index of each char
        
#         for i, c in enumerate(s):
#             if c not in in_seen:
#                 # remove previous characters that are bigger (to get smaller lexicographically)
#                 # and still appear later in the string
#                 while seen and c < seen[-1] and i < last_occurrence[seen[-1]]:
#                     removed = seen.pop()
#                     in_seen.remove(removed)
#                 seen.append(c)
#                 in_seen.add(c)
        
#         return ''.join(seen)

        # seen = []
        # for i in s :
        #     if i not in seen:
        #         seen.append(i) 
        # return ''.join(sorted(seen))
      

        