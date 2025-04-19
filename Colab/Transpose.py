matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#trasop = [[ row[col] for row in matrix ] for col in range(len(matrix[0]))]

def transpose(mat):
    transpose = []
    for col in range(len(matrix[0])):
      cur = []
      for row in matrix:
          cur.append(row[col])
      transpose.append(cur)
    return transpose


print(transpose(matrix))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using list comprehension to transpose the matrix
# transpose = [[ row[col] for row in matrix ] for col in range(len(matrix[0]))]

t= [[ row[col] for row in matrix ] for col in range(3)]
print(t)