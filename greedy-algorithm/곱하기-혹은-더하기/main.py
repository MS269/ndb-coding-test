str = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(str[0])

# 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행
for i in range(1, len(str)):
    num = int(str[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
