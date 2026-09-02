# n, m => 세로줄, 가로줄
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def runLadder(edges):
    result = [0]*(n+1)
    for i in range(1, n+1):
        floor = 0

        pos = i
        for x1, x2 in edges:
            # 지나갈 선분을 찾으면 이동
            if x2 <= floor:
                continue

            if x1 == pos:
                floor = x2
                pos = x1+1
            elif x1 == pos-1:
                floor = x2
                pos = x1

        result[i] = pos
    return result

def resolve_line(lines, idx):
    global result

    # 검증
    answer = runLadder(lines)
    # print(f'{lines}: {answer}')
    if answer == cur:
        result = min(result, len(lines))
        return

    if len(lines) >= result:
        return
    
    for i in range(idx, len(edges)):
        lines.append(edges[i])
                
        resolve_line(lines, i+1)
        lines.pop()


edges.sort(key=lambda x:x[1])
# 초기 정답 값 지정
cur = runLadder(edges)
result = float('inf')
resolve_line([], 0)
print(result)