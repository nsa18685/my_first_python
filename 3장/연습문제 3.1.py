# 오각형의 넓이 구하기
import math

r = eval(input("중심에서 꼭짓점까지의 길이를 입력하세요. ex,5.5: "))
s = 2 * r * math.sin(math.pi/5)
넓이 = ((3 * (pow(3, (1 / 2)))) / 2) * (pow(s, 2))

print("오각형의 넓이는", round(넓이, 2), "입니다.")
