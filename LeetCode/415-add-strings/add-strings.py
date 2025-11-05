class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            x1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            x2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            value = x1 + x2 + carry
            carry = value // 10
            result.append(str(value % 10))
            i -= 1
            j -= 1

        return ''.join(reversed(result))



# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         num1 = int(num1)
#         num2 = int(num2)
#         return str(num1 + num2)