n, k = map(int, input().split())
num = list(input())

cnt = 0
stack = []
for i in num:
    while cnt < k and stack and stack[-1] < i:
        stack.pop()
        cnt += 1

    stack.append(i)

print("".join(stack[:n - k]))
