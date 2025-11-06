class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        arr = []
        while num != 0:
            a = num % 7
            arr.append(str(a))
            num //= 7
        
        result = ''.join(reversed(arr))

        if negative:
            return '-' + result
        else:
            return result




# class Solution:
#     def convertToBase7(self, num: int) -> str:
#         arr = []
#         while num % 7 == 0:
#             a = num % 7
#             arr.append(a)
#         return str(arr)