n = int(input())
s = input()

cnt = s.count("LL")

print(min(n, n - cnt + 1))
