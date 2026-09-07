N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# N: 턴수, M: 마지막 칸, K: 말의 수
def dfs(dept):
    global result
    if dept == N:
        result = max(result, len([i for i in roc if i >= M]))
        return

    for i in range(K):
        roc[i] += nums[dept]
        dfs(dept+1)
        roc[i] -= nums[dept]

roc = [1]*K
result = 0
dfs(0)
print(result)