N = int(input())

def dfs(dept):
    if dept >= N:
        print(' '.join(map(str, selected)))

    for i in range(N, 0, -1):
        if i in selected:
            continue

        selected.append(i)
        dfs(dept+1)
        selected.pop()

selected = []
dfs(0)
