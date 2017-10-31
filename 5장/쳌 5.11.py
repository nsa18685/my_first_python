# 다음 프로그램의 출력값을 보이시오
print('(a)')
for i in range(1, 5):
    j = 0
    while j < i:
        print(j, end = '')
        j += 1

print('\n\n(b)')
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = '')
    print("****")
    i += 1

print('\n(c)')
i = 5
while i >= 1:
    num = 1
    for j in range(1, i + 1):
        print(num, end = "xxx")
        num *= 2
    print()
    i -= 1

print('\n(d)')
i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1):
        print(num, end = 'G')
        num += 2
    print()
    i += 1
