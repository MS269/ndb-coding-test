s = input()

s = s.replace("XX", "BB")
s = s.replace("BBBB", "AAAA")

print(s if "X" not in s else -1)
