class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        st = 0
        max_l = 0
        for i in range(len(s)):
            c = s[i]
            if c in seen and seen[c] >= st:
                st = seen[c] + 1
            seen[c] = i
            max_l = max(max_l , i-st+1)
        return max_l


        # arr = list(s)
        # seen = set()
        # maxl = 0
        # count = 0
        # for i in arr:
        #     if i in seen:
        #         seen.clear()  
        #         count = 0     
        #     seen.add(i)
        #     count += 1
        #     maxl = max(maxl, count)
        # return maxl


        # arr = list(s)
        # count = 0
        # seen = set()
        # maxl = 0
        # for i in arr:
        #     if i in seen:
        #         count -= 1
        #         seen.pop()
        #     else:
        #         count += 1

        #     maxl = max(maxl , len(seen))
        #     seen.add(i)
        # return count



        # start =0
        # k = len(s)
        # max_len = 0
        # seen = {}
        # for end in range(len(s)):
        #     curr_char = s[end]
        #     if curr_char in seen and seen[curr_char] >= start:
        #         start = seen[curr_char] + 1
        #     seen[curr_char] = end
        #     max_len = max(max_len, end - start + 1)
        # return max_len

        