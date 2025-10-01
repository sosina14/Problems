class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] == target:
                return i+1,j+1
                break
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1
            















        # i = 0
        # j = len(numbers)-1
        # cur_sum = 0
        # while i < j:
        #     cur_sum = numbers[i] + numbers[j]
        #     if cur_sum == target:
        #         return [i+1, j+1]
        #         break
        #     elif cur_sum < target:
        #         i += 1
        #     else:
        #         j-= 1
        # return []
        