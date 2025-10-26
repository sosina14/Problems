class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()
            else:
                return False 

        return len(stack) == 0
