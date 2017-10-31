num = eval(input("수를 입력하세요: "))

num = True if 0 < num <= 100 or num < 0 else False
print(num)
