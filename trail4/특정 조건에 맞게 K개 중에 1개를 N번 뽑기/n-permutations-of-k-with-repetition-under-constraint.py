K, N = map(int, input().split())

# Please write your code here.
def dfs(dept):
    global result
    if dept == N:
        result.append(selected[:])
        return

    for i in range(1, K+1):
        if dept == 0 or dept == 1 or i != selected[-1] or i != selected[-2]:
            selected.append(i)
            dfs(dept+1)
            selected.pop()

result = []
selected = []
dfs(0)
for cur in result:
     print(' '.join(map(str, cur)))