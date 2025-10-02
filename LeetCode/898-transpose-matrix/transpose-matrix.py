class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t = []
        for c in range(len(matrix[0])):
            x = []
            for r in matrix:
                x.append(r[c])
            t.append(x)
        return t 
