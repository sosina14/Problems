#Best way
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for num in zip(*matrix):
  print(num)