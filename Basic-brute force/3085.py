def count_adjacent_cells(matrix):
    counts = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    max_counts = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_cell = matrix[i][j]
            
            if j > 0 and current_cell == matrix[i][j - 1]:
                counts[current_cell] += 1
            else:
                max_counts[current_cell] = max(max_counts[current_cell], counts[current_cell])
                counts[current_cell] = 1
    
    return max(max_counts.values())

def swap_and_count(matrix, i, j, new_i, new_j):
    matrix[i][j], matrix[new_i][new_j] = matrix[new_i][new_j], matrix[i][j]
    return count_adjacent_cells(matrix)

N = int(input())
Bombo = [list(input()) for _ in range(N)]
max_count = count_adjacent_cells(Bombo)

for i in range(N):
    for j in range(N):
        if j + 1 < N and Bombo[i][j] != Bombo[i][j + 1]:
            new_count = swap_and_count(Bombo, i, j, i, j + 1)
            max_count = max(max_count, new_count)
            swap_and_count(Bombo, i, j, i, j + 1)  # 원래대로 되돌림

        if i + 1 < N and Bombo[i][j] != Bombo[i + 1][j]:
            new_count = swap_and_count(Bombo, i, j, i + 1, j)
            max_count = max(max_count, new_count)
            swap_and_count(Bombo, i, j, i + 1, j)  # 원래대로 되돌림

print(max_count)
