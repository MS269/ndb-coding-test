s = input()

alphabets = [0] * 26
for i in s:
    alphabets[ord(i) - 65] += 1

front = ""
odd_alphabet = ""
for i in range(26):
    front += chr(i + 65) * (alphabets[i] // 2)

    if alphabets[i] % 2 == 1:
        odd_alphabet += chr(i + 65)

if len(odd_alphabet) <= 1:
    print(front + odd_alphabet + front[::-1])
else:
    print("I'm Sorry Hansoo")
