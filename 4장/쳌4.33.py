# if / else 명령문으로 조건식 재작성하기

#(a)
#score = 3 * scale if x < 10 else 4 * scale
if x < 10:
    score = 3 * scale
else:
    score = 4 * scale

#(b)
#tax = income * 0.2 if income > 1000 else income * 0.17 + 1000
if income > 1000:
    tax = income * 0.2
else:
    tax = income * 0.17 + 1000

#(c)
# print(i if number % 3 == 0 else j)
if number % 3 == 0
    print(i)
else:
    print(j)
