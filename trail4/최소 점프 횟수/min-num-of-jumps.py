from collections import deque

N = int(input())
num = list(map(int, input().split()))

# Please write your code here.
# N: 각 위치로부터의 최대 점프 가능 거리 개수

def bfs():
    q = deque([0])

    count = 0
    while q:
        for _ in range(len(q)):
            pos = q.popleft()

            if pos == N-1:
                return count

            # cur보다 이하의 칸수를 이동
            for i in range(1, num[pos]+1):
                if pos+i <= N-1:
                    q.append(pos+i)

        count += 1

    return -1

print(bfs())