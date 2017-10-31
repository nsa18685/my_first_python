# 5.11 break문없이 재작성
sum = 0
number = 0

while sum <= 100:
    number += 1
    sum += number
print("마지막 숫자는", number,"입니다.")
print("합계는", sum,"입니다.")
               

# 5.12 continue문 없이 재작성
sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        sum = sum
    else:
        sum += number

print("합계는", sum, "입니다.")
