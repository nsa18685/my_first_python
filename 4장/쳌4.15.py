count = eval(input("count를 입력하시오: "))

'''
if count % 10 == 0:
    newLine = True
else:
    newLine = True
print(newLine)
'''

# 위의 식, 부울식을 사용하여 재작성하기

newLine = True if count % 10 == 0 else False
print(newLine)
