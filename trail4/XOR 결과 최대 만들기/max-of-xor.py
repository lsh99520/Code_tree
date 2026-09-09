N, M = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def dfs(dept, idx):
    global result
    if dept >= M:
        temp = 0
        for num in selected:
            temp ^= num

        result = max(result, temp)
        return

    for i in range(idx, len(A)):
        selected.append(A[i])
        dfs(dept+1, i+1)
        selected.pop()

selected = []
result = 0
dfs(0, 0)
print(result)