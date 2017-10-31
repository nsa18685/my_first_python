weight = eval(input("몸무게를 입력하세요: "))
height = eval(input("키를 입력하세요: "))

print((weight > 50 or height > 160) and (not (weight > 50 and height > 160)))
