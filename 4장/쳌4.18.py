income = eval(input("수입을 입력하세요: "))


if income <= 10000:
    tax = income * 0.1
elif income <= 20000:
    tax = 1000 + \
          (income - 10000) * 0.15
print("세금은", tax, "입니다.")

'''
# True and False -> False 
if income <= 10000:
    tax = income * 0.1
elif income <= 10000 and income <= 20000:
    tax = 1000 + \
          (income - 10000) * 0.15
print("세금은", tax, "입니다.")
'''
