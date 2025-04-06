matrix = []

for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(value)
    matrix.append(row)

for r in matrix:
    print(r)
