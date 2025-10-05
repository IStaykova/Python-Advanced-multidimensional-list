n = int(input())
matrix = []

for row in range(n):
    matrix.append([])
    for column in input().split():
        matrix[row].append(int(column))

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))