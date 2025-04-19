matrix = []

for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(value)
    matrix.append(row)

print ('  The Matrix is of user input\n')
for r in matrix:
    print(r)
print("\n The transpose of the matrix user intured \n")
for n in zip(*matrix):
    print(n)

