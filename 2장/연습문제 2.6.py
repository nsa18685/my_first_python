#정수의 자릿수 합산하기

정수 = eval(input("0과 1000 사이의 숫자(정수)를 입력하세요: "))

합 = (정수 % 10) + (정수 // 10 % 10) + (정수 // 10 // 10 % 10)

print("각 자릿수의 합은", 합, "입니다.")
