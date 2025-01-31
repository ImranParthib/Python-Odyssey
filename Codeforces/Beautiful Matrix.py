# Read the 5x5 matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the position of the '1'
found = False
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row, col = i, j
            found = True
            break
    if found:
        break

# Calculate the minimum number of moves
moves = abs(row - 2) + abs(col - 2)
# # Print the matrix
# for i in range(5):
#     for j in range(5):
#         print(matrix[i][j], end=" ")
#     print()
 
print (moves)

    

# Time complexity: O(1)
# Space complexity: O(1)
# Difficulty: easy
# Tags: implementation
# Concepts: Manhattan distance
