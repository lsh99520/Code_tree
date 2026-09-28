def dfs(dept, idx):
    global result

    if dept >= N:
        result = min(result, abs((total-sum(selected_A)) - sum(selected_A)))

    for i in range(idx, len(nums)):
        if len(selected_A) < N:
            selected_A.append(nums[i])
            dfs(dept+1, i+1)
            selected_A.pop()

N = int(input())
nums = list(map(int, input().split()))
selected_A = []
result = float('inf')
total = sum(nums)

dfs(0, 0)

print(result)