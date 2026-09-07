N = int(input())

# Please write your code here.
def dfs(arr):
    if len(arr) == N:
        return ''.join(map(str, arr[:]))

    for selected in [4, 5, 6]:
        error = False

        arr.append(selected)
        for size in range(1, len(arr)//2 + 1):
            if arr[-(size*2): -size] == arr[-size:]:
                error = True
                break

        if not error:
            result = dfs(arr)
            if result:
                return result
        
        arr.pop()

print(dfs([]))