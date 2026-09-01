n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

b1r = [-2, -1, 0, 1, 2]
b1c = [0, 0, 0, 0, 0]

b2r = [-1, 1, 0, 0, 0]
b2c = [0, 0, -1, 1, 0]

b3r = [-1, -1, 1, 1, 0]
b3c = [-1, 1, -1, 1, 0]

div = [[b1r, b1c], [b2r, b2c], [b3r, b3c]]

boom = [[0] * n for _ in range(n)]

result = 0
count = 0


def dfs(dept):
    global result, count

    if dept == len(bombs):
        result = max(result, count)
        return

    r, c = bombs[dept]

    for dr, dc in div:
        affected = []

        for i in range(5):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue

            if boom[nr][nc] == 0:
                count += 1

            boom[nr][nc] += 1
            affected.append((nr, nc))

        dfs(dept + 1)

        for nr, nc in affected:
            boom[nr][nc] -= 1

            if boom[nr][nc] == 0:
                count -= 1


dfs(0)

print(result)