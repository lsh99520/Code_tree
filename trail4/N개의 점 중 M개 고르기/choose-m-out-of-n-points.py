def dfs(dept, idx, max_dist):
    global result

    if dept >= M:
        result = min(result, max_dist)
        return

    for i in range(idx, N):
        i_x, i_y = points[i]

        next_dist = max_dist

        if len(selected) > 0:
            for x, y in selected:
                next_dist = max(next_dist, get_dist(x, i_x, y, i_y))

        selected.append(points[i])
        dfs(dept + 1, i + 1, next_dist)
        selected.pop()


def get_dist(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

selected = []
result = float('inf')

dfs(0, 0, 0)

print(result)