N, M = map(int, input().split())

# Please write your code here.
# 1 이상 N 이하 정수 중, M개 조합

def dfs(dept, idx):
    if dept >= M:
        print(*selected)
        return

    for i in range(idx, N+1):
        selected.append(i)
        dfs(dept+1, i+1)
        selected.pop()

selected = []
dfs(0, 1)