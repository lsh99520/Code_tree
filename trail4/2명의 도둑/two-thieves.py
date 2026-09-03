N, M, C = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(N)]


def get_max_value(idx, total_weight, total_value):
    global max_value

    if total_weight > C:
        return

    max_value = max(max_value, total_value)

    for i in range(idx, len(weight_li)):
        get_max_value(i+1, total_weight + weight_li[i], total_value + weight_li[i] ** 2)

def selected_max_value(total_value, dept, r, c):
    global result

    if dept >= 2:
        result = max(result, total_value)
        return

    for i in range(r, len(values)):
        if i == r:
            start_c = c
        else:
            start_c = 0

        for j in range(start_c, len(values[0])):

            if j + M < len(values[0]):
                nr = i
                nc = j + M
            else:
                nr = i + 1
                nc = 0

            selected_max_value(total_value + values[i][j], dept + 1, nr, nc)

weight_li = []
max_value = 0

values = [[0]*(N-M+1) for _ in range(N)]

for i in range(N):
    for j in range(N-M+1):

        for z in range(M):
            weight_li.append(weight[i][j+z])

        max_value = 0
        get_max_value(0, 0, 0)

        values[i][j] = max_value

        weight_li.clear()

result = 0
selected_max_value(0, 0, 0, 0)
print(result)