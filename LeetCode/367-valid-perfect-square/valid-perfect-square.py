class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        for i in range(num):
            if i * i == num or num == 1:
                return True
            if i * i > num:
                return False
  
            