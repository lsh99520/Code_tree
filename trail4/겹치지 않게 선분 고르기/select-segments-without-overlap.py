n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)


def dfs(idx, depth):
    global result

    result = max(result, depth)

    for i in range(idx, n):
        r1, r2 = x1[i], x2[i]
        start = min(r1, r2)
        end = max(r1, r2)

        if seleted[start:end + 1].count(1) != 0:
            continue

        affected = []

        for j in range(start, end + 1):
            seleted[j] = 1
            affected.append(j)

        dfs(i + 1, depth + 1)

        for j in affected:
            seleted[j] = 0


seleted = [0] * (max(max(x1), max(x2)) + 1)
result = 0

dfs(0, 0)

print(result)