def check_visited(r, c, check):
    for i in range(N):
        visited[r][i] += check
        visited[i][c] += check

def dfs(dept):
    global result

    if dept >= N:
        result = max(result, sum(selected))
        return

    for c in range(N):
        if visited[dept][c]:
            continue
        selected[dept] = grid[dept][c]
        check_visited(dept, c, 1)
        dfs(dept+1)
        selected[dept] = 0
        check_visited(dept, c, -1)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0]*N for _ in range(N)]
selected = [0]*N

dfs(0)
print(result)