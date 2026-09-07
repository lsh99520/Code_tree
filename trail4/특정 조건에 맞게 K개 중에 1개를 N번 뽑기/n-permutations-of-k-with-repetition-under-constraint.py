K, N = map(int, input().split())

# Please write your code here.
def dfs(dept):
    if dept == N:
        print(*selected[:])
        return

    for i in range(1, K+1):
        if dept == 0 or dept == 1 or i != selected[-1] or i != selected[-2]:
            selected.append(i)
            dfs(dept+1)
            selected.pop()

selected = []
dfs(0)