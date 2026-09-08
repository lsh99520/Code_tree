expression = input()

# a~f 까지 알파벳, +,-,* => 길이 N
# 알파벳 중 1~4 이하의 정수 대입 => 식의 결과 최대
# 사칙연산 계산 순서가 동일

def dfs(dept, total):
    global result

    if dept >= len(expression):
        result = max(result, total)
        return

    cur = alphabet_num[alphabet.index(expression[dept])]

    if cur != 0:
        calc = [total + cur, total - cur, total * cur]
        dfs(dept + 2, calc[operators.index(expression[dept - 1])])

    else:
        for i in [1, 2, 3, 4]:
            calc = [total + i, total - i, total * i]
            alphabet_num[alphabet.index(expression[dept])] = i
            dfs(dept + 2, calc[operators.index(expression[dept - 1])])
            alphabet_num[alphabet.index(expression[dept])] = 0


operators = ['+', '-', '*']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
alphabet_num = [0] * 6
result = float('-inf')

for i in [1, 2, 3, 4]:
    alphabet_num[alphabet.index(expression[0])] = i
    dfs(2, i)

print(result)