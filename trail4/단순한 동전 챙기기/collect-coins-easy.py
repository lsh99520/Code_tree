from collections import deque

def bfs():
    q = deque([(sr, sc, 0, 0, 0)])

    visited = [[[[-1] * N for _ in range(N)] for _ in range(10)] for _ in range(10)]

    visited[0][0][sr][sc] = 1

    while q:
        r, c, dept, coin_cnt, coin_val = q.popleft()

        if grid[r][c] == 'E' and coin_cnt >= 3:
            return dept

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if visited[coin_val][coin_cnt][nr][nc] == -1:
                visited[coin_val][coin_cnt][nr][nc] = 1
                q.append((nr, nc, dept+1, coin_cnt, coin_val))

            if grid[nr][nc].isdigit():
                next_coin = int(grid[nr][nc])

                if next_coin > coin_val:
                    if visited[next_coin][coin_cnt+1][nr][nc] == -1:
                        visited[next_coin][coin_cnt+1][nr][nc] = 1
                        q.append((nr, nc, dept+1, coin_cnt+1,next_coin))
    return -1

N = int(input())
grid = [list(input()) for _ in range(N)]

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

for r in range(N):
    for c in range(N):
        if grid[r][c] == 'S':
            sr, sc = r, c

print(bfs())