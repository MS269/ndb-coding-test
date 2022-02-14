n = int(input())
words = [list(map(lambda x: ord(x) - ord("A"), input()))
         for _ in range(n)]
alphabets = [0] * 26

for i in range(n):
    for j in range(1, len(words[i]) + 1):
        alphabets[words[i][-j]] += 10 ** (j - 1)

alphabets.sort(reverse=True)

ans = 0
num = 9
for i in range(26):
    if alphabets[i] == 0:
        break
    ans += (num * alphabets[i])
    num -= 1

print(ans)
