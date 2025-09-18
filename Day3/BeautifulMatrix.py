matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find where the 1 is
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row, col = i+1, j+1  # 1-based indexing
            break

# Minimum moves to center (3,3)
moves = abs(row - 3) + abs(col - 3)
print(moves)
