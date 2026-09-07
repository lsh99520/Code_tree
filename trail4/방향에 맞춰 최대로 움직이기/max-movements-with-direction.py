N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
move_dir = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())

# Please write your code here.
# N: 칸 수, num: 각 칸의 크기, move_dir: 방향, R, C: 시작 위치
def dfs(dept, r, c):
    global result
    result = max(result, dept)

    div = move_dir[r][c]
    cur = num[r][c]
    while True:
        nr = r + dr[div]
        nc = c + dc[div]

        if nr < 0 or nc < 0 or N <= nr or N <= nc:
            break

        if num[nr][nc] > cur:
            dfs(dept+1, nr, nc)

        r = nr
        c = nc
    

dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

result = 0
dfs(0, R-1, C-1)
print(result)